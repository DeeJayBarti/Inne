from netaddr import *

import subprocess
import sys
import pprint

for IP in IPNetwork('156.17.86.0/24','156.17.87.0/24'): # Dla danych adresow 
    str_IP =str(IP)
    subp = subprocess.run(['netcat', '-w 1', str_IP, '80'])
    if (subp.returncode!=0):
        pass
    else:
    	dig = subprocess.run(['dig', '-x',str_IP, '+short'], stdout=subprocess.PIPE)
    	nazwa = str(dig.stdout.decode('utf-8'))
    	p = str_IP[0:3]
    	d = str_IP[4:6]
    	t = str_IP[7:9]
    	host = subprocess.run(["host -t soa "+t+"."+d+"."+p+".in-addr.arpa | cut -d' ' -f6 | sed 's/\./\@/' | sed 's/\.$//'"],shell=True,stdout=subprocess.PIPE) # Zwracanie ip serwera
    	poczta = str(host.stdout.decode('utf-8'))
    	serwer = subprocess.Popen("HEAD "+str_IP+" | grep Server", shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
print(nazwa+";"+str_IP+";"+serwer+";"+poczta)
