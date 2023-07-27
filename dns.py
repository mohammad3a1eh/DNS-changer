from os import system
import argparse







def auto():
    system('netsh interface ipv4 set dnsservers "Wi-Fi" dhcp')
    system("ipconfig /flushdns")
            

def google():
    system('netsh interface ipv4 set dns name="Wi-Fi" static 8.8.8.8 primary')
    system('netsh interface ipv4 add dns name="Wi-Fi" addr=8.8.4.4 index=2')
    system("ipconfig /flushdns")
        
        
def shecan():
    system('netsh interface ipv4 set dns name="Wi-Fi" static 178.22.122.100 primary')
    system('netsh interface ipv4 add dns name="Wi-Fi" addr=185.51.200.2 index=2')
    system("ipconfig /flushdns")


def onepointone():
    system('netsh interface ipv4 set dns name="Wi-Fi" static 1.1.1.1 primary')
    system('netsh interface ipv4 add dns name="Wi-Fi" addr=1.0.0.1 index=2')
    system("ipconfig /flushdns")


def electro():
    system('netsh interface ipv4 set dns name="Wi-Fi" static 78.157.42.101 primary')
    system('netsh interface ipv4 add dns name="Wi-Fi" addr=78.157.42.100 index=2')
    system("ipconfig /flushdns")        
        

def radar():
    system('netsh interface ipv4 set dns name="Wi-Fi" static 10.202.10.10 primary')
    system('netsh interface ipv4 add dns name="Wi-Fi" addr=10.202.10.11 index=2')
    system("ipconfig /flushdns")    
        
def char03():
    system('netsh interface ipv4 set dns name="Wi-Fi" static 10.202.10.202 primary')
    system('netsh interface ipv4 add dns name="Wi-Fi" addr=10.202.10.102 index=2')
    system("ipconfig /flushdns")        
        
        
   
        
        
parser = argparse.ArgumentParser(description="set and change DNS Wifi module")
parser.add_argument("-ip","--ip",help="get name DNS")


args = parser.parse_args()

if args.ip == "google":
    google()
elif args.ip == "auto":
    auto()
elif args.ip == "shecan":
    shecan()
elif args.ip == "1.1.1.1":
    onepointone()
elif args.ip == "electro":
    electro()
elif args.ip == "radar":
    radar()
elif args.ip == "403":
    char03()
else:
    print("""
argument support :

    * auto
    * google
    * shecan
    * 1.1.1.1
    * electro
    * radar
    * 403
    
example :

    * python DNS.py -ip google
    * dns.exe -ip google
    * dns -ip google
    * python DNS.py --ip google
    * dns.exe --ip google
    * dns --ip google
          """)