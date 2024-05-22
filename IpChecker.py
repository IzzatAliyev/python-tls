import ipaddress

def isValidIPv4OrIPv6Address(ip_string):
    try:
        check = ipaddress.ip_address(ip_string)
        print(f"{check} is the valid IP")
    except:
        print(f"Invalid IP address: {ip_string}")

ip_str = input("Enter the IP address: ")
    
isValidIPv4OrIPv6Address(ip_str)