# Task 1
def palindrom(text):
    words = text.split()
    palindromes = []
    for word in words:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes

text = "kayak deified work word world civic noon"
palindromes = palindrom(text)
print(palindromes)

# Task 2
import re

def validate_ip(ip_address):
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    match = re.match(pattern, ip_address)
    if match:
        octets = ip_address.split('.')
        for octet in octets:
            if int(octet) > 255:
                return False
        return True
    else:
        return False

ip_address = '192.168.0.0'
is_valid = validate_ip(ip_address)
print(is_valid)

# Task 3
import platform

def get_os():
    os_name = platform.system()
    if os_name == 'Darwin':
        return 'Mac'
    elif os_name == 'Windows':
        return 'Windows'
    elif os_name == 'Linux':
        return 'Linux'
    else:
        return 'Unknown'

os_name = get_os()
print(os_name)