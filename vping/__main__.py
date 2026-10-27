#!/usr/bin/env python3

# File: vping/__main__.py
# Author: Hadi Cahyadi <cumulus13@gmail.com>
# Date: 2026-10-27
# Description: 
# License: MIT

import sys
from .core import ping

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m vping <hostname_or_ip>")
        sys.exit(1)
        
    host = sys.argv[1]
    print(f"Checking target: {host} ...")
    
    alive = ping(host)
    if alive:
        print(f"RESULT: {host} is ALIVE")
        sys.exit(0)
    else:
        print(f"RESULT: {host} is DOWN / UNREACHABLE")
        sys.exit(1)

if __name__ == "__main__":
    main()