import random

def IPv6_generator():
    IPv6 = []
    for i in range(8):
        block = random.randint(0, 65535).to_bytes(2, byteorder='big').hex()
        if len(block) == 1:
            block = '0' + block
        IPv6.append(block)
    IPv6 = ':'.join(IPv6)
    print(IPv6)

IPv6_generator()
