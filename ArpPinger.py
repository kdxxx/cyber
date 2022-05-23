import argparse
import scapy.all as scapy

class ARPPing():
    def __int__(self):
        print("ARPPing is starting...")

    def get_user(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-i','--ipaddress',type=str,help="IP adresinizi girmelisiniz")
        args = parser.parse_args()
        #print(args.ipaddress)
        if args.ipaddress != None:
            return args
        else:
            print("Ip Adresini girsene")

    def arp_request(self,ip):
            #scapy.arp => hangi ıp adresi
            # fff => Broadcast olacak diyor

            #Açıklama
            arp_request_packet = scapy.ARP(pdst=ip)
            broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            combined_packet = broadcast_packet / arp_request_packet
            answered_list, unanswered_list = scapy.srp(combined_packet,timeout = 1)
            answered_list.summary()  # print ediyor


            #ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst="192.168.1.0/24"), timeout=2)
            #ans.summary()


if __name__ =="__main__":
    arp_ping = ARPPing() # obje oluşturmak zorundayız
    kullanıcı_girdisi = arp_ping.get_user()
    arp_ping.arp_request(kullanıcı_girdisi.ipaddress)
    # kullanıcı istediği Ip adresini sorgulayabilir (netdiscover)
    
