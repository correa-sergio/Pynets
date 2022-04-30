#!/usr/bin/python

# Title: PyNetS - Python Network Scanner
# Developed by Sérgio Corrêa
# Tested on: MacOS / Linux

import socket
import time
import sys
import argparse
import ipaddress



class Color:
    RED = '\033[1;31;48m'
    GREEN = '\033[1;32;48m'
    END = '\033[1;37;0m'


parser = argparse.ArgumentParser(prog="PyNets", description="PyNets - Python Network Scanner 1.0",
                                usage="Ex: python3 pynets.py -i 192.168.0.6 -p 22")
parser.add_argument("-i", "--ip", help="The address reflected to the target ", type=ipaddress.ip_address)
parser.add_argument("-p", "--port", type=int, nargs='*', help="The port reflected to the target ")
parser.add_argument("-v", "--version", action='version', version='%(prog)s 1.0')

banner = '''[√] PyNetS - Python Network Scanner v.1.0\n'''

parsed_arguments = parser.parse_args()

ip = str(parsed_arguments.ip)

port = parsed_arguments.port

port_list = []

cont = 0

if not ip or not port:

        parser.print_help()

        sys.exit()


print(Color.GREEN + "[√] IP address '%s' is valid" % ip + Color.END)
        
start_time = time.time()        
    
for porta in port:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        
        socket.setdefaulttimeout(0.2)
                   
        if (sock.connect_ex((ip,porta)) == 0 ):
                
                port_list.append(porta)
                
                sock.close()
                
                cont += 1
                
for check in port_list:
        
        print(Color.GREEN + '[√] Found Port: {}'.format(check) + Color.END)


end_time = time.time()

total_time = end_time - start_time

print(Color.GREEN + '[√] Total of {}'.format(cont) + ' port(s) opened' + Color.END)

print('\n[√] Processing Time:', total_time)

print(banner)

