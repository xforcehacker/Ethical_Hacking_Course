import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcat = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_reques_broadcast = broadcat/arp_request
    answered_list = scapy.srp(arp_reques_broadcast, timeout=1)[0]
    for element in answered_list:
        #PRINT IP ADDRESS
        print(element[1].psrc)
        #PRINT MAC ID
        print(element[1].hwsrc)
        print("-------------------------------------------")

#SCANNING SUBNET
scan("192.168.1.1/24")