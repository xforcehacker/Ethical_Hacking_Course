import optparse
import scapy.all as scapy
from optparse import OptParseError, OptionParser 

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP / IP range.")
    options, arguments = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcat = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_reques_broadcast = broadcat/arp_request
    # VERBOSE IS OFF DETAIL WILL NOT BE DISPLAYED
    answered_list = scapy.srp(arp_reques_broadcast,
                              timeout=1, verbose=False)[0]
 
    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
        # PRINT IP ADDRESS
        #print(element[1].psrc + "\t\t" + element[1].hwsrc)

    return client_list

def print_result(results_list):

    print("\nIP\t\t\tMAC Address\n-------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)