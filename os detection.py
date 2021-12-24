from scapy.all import *
from scapy.layers.inet import IP, ICMP


os = ''
target = input("Enter the Ip address:")
pack = IP(dst=target)/ICMP()
resp = sr1(pack, timeout=3)
if resp:
    if IP in resp:
        ttl = resp.getlayer(IP).ttl
        if ttl <= 64: 
            os = 'Linux'
        elif ttl > 64:
            os = 'Windows'
        else:
            print('Not Found')
        print(f'\n\nTTL = {ttl} \n*{os}* Operating System is Detected \n\n')
