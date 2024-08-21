def is_valid_octet(octet):
    if len(octet) == 0 or len(octet) > 3:
        return False
    if octet[0] == '0' and len(octet) > 1:  
        return False
    return 0 <= int(octet) <= 255

def generate_ip_addresses(s):
    n = len(s)
    valid_ips = []

    for i in range(1, min(4, n - 2)): 
        for j in range(i + 1, min(i + 4, n - 1)):  
            for k in range(j + 1, min(j + 4, n)): 
                octet1 = s[:i]
                octet2 = s[i:j]
                octet3 = s[j:k]
                octet4 = s[k:]

                if (is_valid_octet(octet1) and
                    is_valid_octet(octet2) and
                    is_valid_octet(octet3) and
                    is_valid_octet(octet4)):
                    valid_ips.append(f"{octet1}.{octet2}.{octet3}.{octet4}")

    return valid_ips

s = input().strip()

result = generate_ip_addresses(s)

for ip in result:
    print(ip)
