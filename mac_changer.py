# Created by Ghost0_0x1
import subprocess
import optparse
import re
import time
#run me in linux

def get_argumet():
    parser=optparse.OptionParser()
    parser.add_option('-i','--interface',dest='network_interface',help='set here network interface')
    parser.add_option('-m','--mac',dest='new_mac',help='set here new mac address')
    option,argumet=parser.parse_args()
    if not option.network_interface:
        parser.error('[-] Specfiy an interface please\n type -h for help ')
    elif not len(option.new_mac)==17:
        parser.error('[-] Please set Mac correctly.')
    elif not option.new_mac:
       parser.error('[-] Specify an mac address please\n type -h for help')
        
    

    return option 


def mac_changer(network_interface,new_mac):
    subprocess.call(f"ifconfig {network_interface} down",shell=True)
    subprocess.call(f"ifconfig {network_interface} hw ether {new_mac}",shell=True)
    subprocess.call(f'ifconfig {network_interface} up',shell=True)
    print(f'[+]Changing Mac address for {network_interface} to {new_mac}')
def get_mac(network_interface):
    ifconfig_reslut= subprocess.check_output(f'ifconfig {network_interface}',shell=True).decode('UTF-8')
    mac_address= re.search('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_reslut)
    return mac_address[0]


option= get_argumet()
mac_changer(option.network_interface,option.new_mac)
mac_address=get_mac(option.network_interface)

if mac_address == option.new_mac:
    
    time.sleep(2)
    print('[+]Mac address has changed successfully.')
else:
    print('[-]something went wrong....')
    print('[-]Run me as aroot')
