# Subnet Calculator v2.0
**Author:** Jonathan Cardoso  
**Language:** Python 3  

## Description
A command-line subnet calculator built in Python that takes an IP address 
and CIDR notation as input and returns key subnet information instantly.
Version 2.0 adds an interactive menu and VLSM (Variable Length Subnet Masking)
support for dividing a network into multiple subnets of different sizes.

## Features
- Network Address
- Subnet Mask
- Broadcast Address
- Usable Host Range
- Total Usable Hosts
- Wildcard Mask
- IP Class Detection (A, B, C, D, E)
- Public/Private IP Detection
- VLSM Calculator *(new in v2.0)*
- Interactive Menu System *(new in v2.0)*

## How to Use
1. Make sure Python 3 is installed on your system
2. Clone or download this repository
3. Open a terminal and navigate to the project folder
4. Run the following command:
`python subnet_calculator.py`
5. Choose from the interactive menu:
   - Option 1: Single Subnet Calculator
   - Option 2: VLSM Calculator
   - q: Quit

## Example Output — Single Subnet
===== Subnet Calculator Results =====
IP Address:        192.168.1.0
CIDR Notation:     /24
Subnet Mask:       255.255.255.0
Wildcard Mask:     0.0.0.255
Network Address:   192.168.1.0
Broadcast Address: 192.168.1.255
Usable Host Range: 192.168.1.1 - 192.168.1.254
Total Usable Hosts: 254
IP Class:          Class C
IP Type:           Private
## Example Output — VLSM
===== VLSM Results for 192.168.1.0/24 =====
Subnet for 50 hosts:
Network:     192.168.1.0/26
Subnet Mask: 255.255.255.192
Hosts:       192.168.1.1 - 192.168.1.62
Usable:      62
Subnet for 25 hosts:
Network:     192.168.1.64/27
Subnet Mask: 255.255.255.224
Hosts:       192.168.1.65 - 192.168.1.94
Usable:      30
Subnet for 10 hosts:
Network:     192.168.1.96/28
Subnet Mask: 255.255.255.240
Hosts:       192.168.1.97 - 192.168.1.110
Usable:      14
## Changelog
### v2.0
- Added VLSM Calculator
- Added interactive menu system

### v1.1
- Added Wildcard Mask calculation
- Added IP Class detection (A, B, C, D, E)
- Added Public/Private IP detection

### v1.0
- Initial release
- Basic subnet calculations

## Future Plans
- v3.0 — Web interface with visual subnet map

## Author
Jonathan Cardoso  
[LinkedIn](https://www.linkedin.com/in/jonathan-costa-cardoso)