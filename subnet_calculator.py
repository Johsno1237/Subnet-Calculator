# Subnet Calculator v1.0
# Author: Jonathan Cardoso
# Description: Takes an IP address and CIDR notation as input
# and returns key subnet information including network address,
# subnet mask, broadcast address, and usable host range.

import ipaddress

def get_subnet_info(ip_cidr):
    network = ipaddress.IPv4Network(ip_cidr, strict=False)
    
    print("\n===== Subnet Calculator Results =====")
    print(f"IP Address:       {ip_cidr.split('/')[0]}")
    print(f"CIDR Notation:    /{network.prefixlen}")
    print(f"Subnet Mask:      {network.netmask}")
    print(f"Network Address:  {network.network_address}")
    print(f"Broadcast Address:{network.broadcast_address}")
    print(f"Usable Host Range:{list(network.hosts())[0]} - {list(network.hosts())[-1]}")
    print(f"Total Usable Hosts:{network.num_addresses - 2}")
    print("=====================================\n")


def main():
    print("\n===== Welcome to Subnet Calculator v1.0 =====")
    print("Author: Jonathan Cardoso\n")
    
    while True:
        ip_cidr = input("Enter IP address with CIDR (e.g. 192.168.1.0/24) or 'quit' to exit: ")
        
        if ip_cidr.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            get_subnet_info(ip_cidr)
        except ValueError:
            print("Invalid input. Please use format: 192.168.1.0/24\n")

if __name__ == "__main__":
    main()   