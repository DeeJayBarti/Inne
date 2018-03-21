from netaddr import *
import subprocess


"""Deklaracja zakresu adresow"""
for IP in IPNetwork('156.17.86.0/24','156.17.87.0/24'):
    str_IP =str(IP)
    a = subprocess.run(['netcat', '-w 1', str_IP, '80'])
    if (a.returncode!=0):
        pass
    else:
        """ Komenda DIG - zwracanie nazwy serwera"""
        dig = subprocess.run(['dig', '-x',str_IP, '+short'], stdout=subprocess.PIPE)
        name = str(dig.stdout.decode('utf-8'))
        """ Komenda HOST - zwracanie ip domeny"""
        first = str_IP[0:3]
        med= str_IP[4:6]
        last = str_IP[7:9]
        host = subprocess.run(["host -t soa "+last+"."+med+"."+first+".in-addr.arpa | cut -d' ' -f6 | sed 's/\./\@/' | sed 's/\.$//'"],shell=True,stdout=subprocess.PIPE)
        mail = str(host.stdout.decode('utf-8'))
        """ Komenda HEAD - zwracanie nazwy serwera"""
        serwer = subprocess.Popen("HEAD "+str_IP+" | grep Server", shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
        """PRINT"""
print(name+";"+str_IP+";"+serwer+";"+mail)
