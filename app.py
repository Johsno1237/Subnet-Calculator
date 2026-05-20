# Subnet Calculator v3.0
# Author: Jonathan Cardoso
# Flask web application for subnet calculations

from flask import Flask, render_template, request
import ipaddress

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        ip_cidr = request.form.get('ip_cidr')
        try:
            network = ipaddress.IPv4Network(ip_cidr, strict=False)
            ip_obj = ipaddress.IPv4Address(ip_cidr.split('/')[0])
            result = {
                'ip': ip_cidr.split('/')[0],
                'cidr': network.prefixlen,
                'subnet_mask': str(network.netmask),
                'wildcard': str(network.hostmask),
                'network_address': str(network.network_address),
                'broadcast': str(network.broadcast_address),
                'host_min': str(list(network.hosts())[0]),
                'host_max': str(list(network.hosts())[-1]),
                'total_hosts': network.num_addresses - 2,
                'ip_class': get_ip_class(ip_obj),
                'ip_type': 'Private' if ip_obj.is_private else 'Public'
            }
        except ValueError:
            error = "Invalid input. Please use format: 192.168.1.0/24"

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)