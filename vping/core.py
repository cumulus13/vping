#!/usr/bin/env python3

# File: vping/core.py
# Author: Hadi Cahyadi <cumulus13@gmail.com>
# Date: 2026-10-27
# Description: 
# License: MIT

import socket
import logging

logger = logging.getLogger("vping")

def _tcp_fallback(host: str, ports: list = None, timeout: float = 1.0) -> bool:
    """Fallback method using TCP connect scans across common ports."""
    if ports is None:
        ports = [80, 443, 53]
        
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                if s.connect_ex((host, port)) == 0:
                    return True
        except Exception:
            continue
    return False


def ping(host: str, timeout: float = 1.0, ports: list = None) -> bool:
    """
    Checks if a host is alive. 
    Tries icmplib first; if missing, unprivileged, or errored, 
    automatically falls back to robust TCP connect scanning.
    """
    # Attempt 1: Try using icmplib if available
    try:
        from icmplib import ping as icmp_ping
        try:
            host_info = icmp_ping(host, count=1, timeout=timeout, privileged=False)
            if host_info.is_alive:
                return True
        except Exception:
            try:
                host_info = icmp_ping(host, count=1, timeout=timeout, privileged=True)
                if host_info.is_alive:
                    return True
            except Exception:
                pass
    except ImportError:
        logger.debug("icmplib not found. Using TCP fallback.")
    except Exception:
        pass

    # Attempt 2: Bulletproof TCP fallback
    return _tcp_fallback(host, ports=ports, timeout=timeout)

