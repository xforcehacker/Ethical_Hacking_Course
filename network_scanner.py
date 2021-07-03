import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcat = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_reques_broadcast = broadcat/arp_request
    #VERBOSE IS OFF DETAIL WILL NOT BE DISPLAYED
    answered_list = scapy.srp(arp_reques_broadcast, timeout=1, verbose=False)[0]
    print("-------------------------------------------")
    print("IP\t\t\t MAC Address\n-------------------------------------------")
    for element in answered_list:
        #PRINT IP ADDRESS
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        

#SCANNING SUBNET
scan("192.168.1.1/24")