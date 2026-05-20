# Subnet Calculator v1.1
# Author: Jonathan Cardoso
# Description: Takes an IP address and CIDR notation as input
# and returns key subnet information including network address,
# subnet mask, broadcast address, usable host range,
# wildcard mask, IP class, and public/private detection..

import ipaddress

def get_ip_class(ip):
    first_octet = int(str(ip).split('.')[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    else:
        return "Class E (Reserved)"

def get_subnet_info(ip_cidr):
    network = ipaddress.IPv4Network(ip_cidr, strict=False)
    ip_obj = ipaddress.IPv4Address(ip_cidr.split('/')[0])
    wildcard = ipaddress.IPv4Address(int(network.hostmask))
    is_private = ip_obj.is_private
    ip_class = get_ip_class(ip_obj)
    
    
    print("\n===== Subnet Calculator Results =====")
    print(f"IP Address:       {ip_cidr.split('/')[0]}")
    print(f"CIDR Notation:    /{network.prefixlen}")
    print(f"Subnet Mask:      {network.netmask}")
    print(f"Network Address:  {network.network_address}")
    print(f"Broadcast Address:{network.broadcast_address}")
    print(f"Usable Host Range:{list(network.hosts())[0]} - {list(network.hosts())[-1]}")
    print(f"Total Usable Hosts:{network.num_addresses - 2}")
    print(f"Wildcard Mask:     {wildcard}")
    print(f"IP Class:          {ip_class}")
    print(f"IP Type:           {'Private' if is_private else 'Public'}")
    print("=====================================\n")


def main():
    print("\n===== Welcome to Subnet Calculator v1.1 =====")
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