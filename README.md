# vping

Fast and robust host alive checker for LAN and WAN networks. Tries native ICMP (`icmplib`) first and automatically falls back to high-performance TCP socket checks if ICMP fails or permissions are restricted.

## Usage

```python
from vping import ping

if ping("8.8.8.8"):
    print("Host is alive!")

```

CLI usage:

```bash
python -m vping 8.8.8.8

```

## 👤 Author
        
[Hadi Cahyadi](mailto:cumulus13@gmail.com)
    

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/cumulus13)

[![Donate via Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cumulus13)
 
[Support me on Patreon](https://www.patreon.com/cumulus13)