# Subnet Calculator v2.0
# Author: Jonathan Cardoso
# Description: Takes an IP address and CIDR notation as input
# and returns key subnet information including network address,
# subnet mask, broadcast address, usable host range,
# wildcard mask, IP class, and public/private detection..
# v2.0 adds multiple subnet support and VLSM (Variable Length Subnet Masking)

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

def vlsm_calculator(network_ip, subnets):
    network = ipaddress.IPv4Network(network_ip, strict=False)
    subnets_sorted = sorted(subnets, reverse=True)
    current_network = network

    print(f"\n===== VLSM Results for {network_ip} =====")
    for hosts_needed in subnets_sorted:
        for prefix in range(32, 0, -1):
            subnet_size = 2 ** (32 - prefix) - 2
            if subnet_size >= hosts_needed:
                subnet = list(current_network.subnets(new_prefix=prefix))[0]
                print(f"\nSubnet for {hosts_needed} hosts:")
                print(f"  Network:    {subnet.network_address}/{prefix}")
                print(f"  Subnet Mask:{subnet.netmask}")
                print(f"  Hosts:      {list(subnet.hosts())[0]} - {list(subnet.hosts())[-1]}")
                print(f"  Usable:     {subnet.num_addresses - 2}")
                current_network = list(current_network.subnets(new_prefix=prefix))[1]
                break
    print("\n=====================================\n")

def main():
    print("\n===== Welcome to Subnet Calculator v2.0 =====")
    print("Author: Jonathan Cardoso\n")

    while True:
        print("Options:")
        print("  1 - Single Subnet Calculator")
        print("  2 - VLSM Calculator")
        print("  q - Quit")
        choice = input("\nEnter your choice: ")

        if choice.lower() == 'q':
            print("Goodbye!")
            break

        elif choice == '1':
            ip_cidr = input("Enter IP address with CIDR (e.g. 192.168.1.0/24): ")
            try:
                get_subnet_info(ip_cidr)
            except ValueError:
                print("Invalid input. Please use format: 192.168.1.0/24\n")

        elif choice == '2':
            network_ip = input("Enter network address with CIDR (e.g. 192.168.1.0/24): ")
            num_subnets = int(input("How many subnets do you need? "))
            subnets = []
            for i in range(num_subnets):
                hosts = int(input(f"How many hosts for subnet {i+1}? "))
                subnets.append(hosts)
            try:
                vlsm_calculator(network_ip, subnets)
            except Exception as e:
                print(f"Error: {e}\n")

        else:
            print("Invalid choice. Please enter 1, 2, or q\n")

if __name__ == "__main__":
    main()