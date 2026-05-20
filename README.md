# Subnet Calculator v1.1
**Author:** Jonathan Cardoso  
**Language:** Python 3  

## Description
A command-line subnet calculator built in Python that takes an IP address 
and CIDR notation as input and returns key subnet information instantly.

## Features
- Network Address
- Subnet Mask
- Broadcast Address
- Usable Host Range
- Total Usable Hosts
- Wildcard Mask *(new in v1.1)*
- IP Class Detection (A, B, C, D, E) *(new in v1.1)*
- Public/Private IP Detection *(new in v1.1)*

## How to Use
1. Make sure Python 3 is installed on your system
2. Clone or download this repository
3. Open a terminal and navigate to the project folder
4. Run the following command:
`python subnet_calculator.py`
5. Enter an IP address with CIDR notation when prompted (e.g. `192.168.1.0/24`)
6. Type `quit` to exit the program

## Example Output
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
=====================================
## Changelog
### v1.1
- Added Wildcard Mask calculation
- Added IP Class detection (A, B, C, D, E)
- Added Public/Private IP detection

### v1.0
- Initial release
- Basic subnet calculations

## Future Plans
- v2.0 — Multiple subnet support and VLSM
- v3.0 — Web interface

## Author
Jonathan Cardoso  
[LinkedIn](https://www.linkedin.com/in/jonathan-costa-cardoso)