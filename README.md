# Subnet Calculator v3.0
**Author:** Jonathan Cardoso  
**Language:** Python 3 | Flask | HTML/CSS

## Description
A full-stack subnet calculator built in Python that started as a simple 
command-line tool and evolved into a complete web application. Enter an 
IP address with CIDR notation and instantly get detailed subnet information 
displayed in a clean, modern web interface.

## Features
- Network Address
- Subnet Mask
- Broadcast Address
- Usable Host Range
- Total Usable Hosts
- Wildcard Mask
- IP Class Detection (A, B, C, D, E)
- Public/Private IP Detection
- VLSM Calculator (command-line)
- Interactive Menu System (command-line)
- ⭐ Web Interface with Flask *(new in v3.0)*

## How to Use

### Web App (v3.0)
1. Make sure Python 3 and Flask are installed
2. Clone or download this repository
3. Open a terminal and navigate to the project folder
4. Run:
`python app.py`
5. Open your browser and go to:
`http://127.0.0.1:5000`
6. Enter an IP address with CIDR and click Calculate

### Command Line (v2.0)
1. Run:
`python subnet_calculator.py`
2. Choose from the menu:
   - Option 1: Single Subnet Calculator
   - Option 2: VLSM Calculator
   - q: Quit

## Project Structure
Subnet Calculator/
│
├── app.py                 # Flask web application
├── subnet_calculator.py   # Command-line version
├── README.md
└── templates/
└── index.html         # Web interface

## Changelog
### v3.0
- Built Flask web application backend
- Designed clean dark-themed HTML/CSS frontend
- Added Private/Public IP badge display

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
- Deploy to cloud (AWS/Heroku) for public access
- Add VLSM support to web interface
- Add subnet visualization map

## Author
Jonathan Cardoso  
[LinkedIn](https://www.linkedin.com/in/jonathan-costa-cardoso) | 
[GitHub](https://github.com/Johsno1237)