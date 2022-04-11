#!/bin/python3
'''
TCP Port Scanner 1.0
- 1kTech
'''
import os, sys, socket
print("\nTCP Port Scanner 1.0\n- 1kTech\n--------")
try:
	ip=sys.argv[1]
	print("Target ip:",ip)
except:
	print("Damn! U dont know enough to use this\nTry: pscan -h")
	sys.exit(1)
if '-h' in sys.argv:
	print("Use: pscan <ip> [-p | ports]\nExample: pscan 127.0.0.1 -p 22,80,443-666")
if '-p' in sys.argv:
	try:
		for i in range(len(sys.argv)):
			if sys.argv[i]=='-p':
				ports=sys.argv[i+1]
				print("Loading ports:",ports,"\n--------")
		ports=ports.split(',')
		for i in range(len(ports)):
			if '-' in ports[i]:
				cut=ports[i]
				del(ports[i])
				cut=cut.split('-')
				#listcut=list(cut[0],cut[1]+1)
				for j in range(int(cut[0]),int(cut[1])+1):
					ports.append(j)
	except:
		print("Damn! An error occurred while selecting ports.\nUsing standard ports.\n--------")
		ports=list(range(1,1024))
else:
	print("Using standard ports.\n--------")
	ports=list(range(1,1024))
try:
	print("Scanning..\n")
	for port in ports:
		client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.05)
		code=client.connect_ex((ip, int(port)))
		if code == 0:
			print(str(port),"open")
except Exception as erro:
	print("Error:", erro)
