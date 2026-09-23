import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument("mask")
args = parser.parse_args()
api = "https://networkcalc.com/api/ip"
class_A = "10.0.0.0"
class_B = "172.16.0.0"
class_C = "192.168.1.0"
mask = args.mask

def api_call(mask):
     api = f"https://networkcalc.com/api/ip/{mask}"
    try:
        response = requests.get(api)
        response.raise_for_status()
        result = response.json()
        
        if result.get("status") != "OK":
            print(f"Error: API returned status '{result.get('status', 'UNKNOWN')}'", file=sys.stderr)
            sys.exit(1)
            
        data = result.get("data", {})
        hosts = data.get("maximum_addresses")
        first_ip = data.get("network_address")
        subnet_mask = data.get("subnet_mask")
        subnet_bits = data.get("cidr")
        
        return hosts, first_ip, subnet_mask, subnet_bits
    except requests.RequestException as e:
        print(f"Error making API request: {e}", file=sys.stderr)
        sys.exit(1)

    data = requests.get(url).json()
    global hosts, first_ip, subnet_mask, subnet_bits

def assignable_hosts(hosts, cidr):
    print("There are",hosts,"assignable hosts for the",cidr,"subnet")

def first_host(first_ip):
    print("The first address is",first_ip)

def mask_decimal(subnet_mask):
    print("The subnet mask in decimal form is", subnet_mask)

def mask_cidr(subnet_bits):
    subnet_bits = str(subnet_bits)
    mask_cidr = "/"+subnet_bits
    print("The subnet mask in cidr notation is", mask_cidr)

if __name__ == '__main__':
    api_call()
    assignable_hosts(hosts, cidr)
    first_host(first_ip)
    mask_decimal(subnet_mask)
    mask_cidr(subnet_bits)
