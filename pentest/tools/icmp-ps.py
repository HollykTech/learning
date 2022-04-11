#!/bin/python3
'''
ICMP Fast Scan
- 1kTech
'''
import ipaddress, socket, struct, time, random, sys
from threading import Thread
#used to create a checksum for the packet
def checksum(source):
	sum=0
	count_to=float(len(source))
	count=0
	while count<count_to:
		thisval=source[count+1]*256+source[count]
		sum=sum+thisval
		sum=sum&0xffffffff
		count=count+2
	if count_to<len(source):
		sum=sum+source[len(source)-1]
		sum=sum&0xffffffff
	sum=(sum>>16)+(sum&0xffff)
	sum=sum+(sum>>16)
	answer=~sum
	answer=answer&0xffff
	answer=answer>>8|(answer<<8&0xff00)
	return answer
#used to create a packet ping
def createpckt(id):
	header=struct.pack('bbHHh',8,0,0,id,1)
	data=192*'Q'
	data=data.encode()
	mychecksum=checksum(header+data)
	header=struct.pack('bbHHh',8,0,socket.htons(mychecksum),id,1)
	return header+data
#used to ping selected address
def ping(addr,port,timeout=1):
	mysocket=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
	idpckt=int((id(timeout)*random.random())%65535)
	pckt=createpckt(idpckt)
	mysocket.connect((addr,port))
	mysocket.sendall(pckt)
	mysocket.close()
#used to ping packets created in list of ips
def rotate(addr,port,filename,wait,responses):
	print("Sending Packets...")
	for ip in addr:
		ping(str(ip),port)
		time.sleep(wait)
	print("All packets sent.\n--------")
	print("Waiting for all responses")
	time.sleep(2) #enough time for hosts to respond
	global signal
	signal=False #turning off signal after sending all packets
	ping('127.0.0.1',port)
	print(len(responses), "hosts found!\n--------")
	hosts=[]
	for response in sorted(responses):
		ip=struct.unpack('BBBB', response)
		ip="{}.{}.{}.{}".format(ip[0],ip[1],ip[2],ip[3])
		hosts.append(ip)
	fhosts=[]
	for i in range(len(hosts)):
		if i==0 or hosts[i]!=hosts[i-1]:
			fhosts.append(hosts[i])
	if filename!=1:
		print("Writting file...")
		global ips
		shosts="Scanned network "+ips+" in port "+str(port)+":\n--------"
		for i in fhosts:
			shosts=shosts+"\n"+str(i)+" up"
		shosts=shosts+"\n--------\nScan ICMP for 1kTech"
		file=open(filename,'w')
		file.write(shosts)
		file.close()
		print("Done!\n")
	else:
		print("Hosts up in port",str(port)+":\n--------")
		for i in fhosts:
			print(str(i),"up")
		print("--------")
#used to listen response ping
def listen(responses):
	global signal
	slisten=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
	slisten.bind(('',1))
	while signal:
		pckt=slisten.recv(1024)[:20][-8:-4]
		responses.append(pckt)
	slisten.close()
def main():
	print("\nICMP Scanner 1.0\n- 1kTech\n--------")
	if '-h' in sys.argv:
		print("Use: icmp-ps <network> [options | -w/p]\nExample: icmp-ps 0.0.0.0/0\n[Options]\n -w for write output in a archive\n -p for use another port\n")
		sys.exit(1)
	try:
		global ips
		ips=sys.argv[1]
		ipnetwork=ipaddress.ip_network(ips,strict=False)
		print("Target network:",ips)
	except:
		print("\nAn error occurred while create a network.\nTry: icmp-ps -h")
		sys.exit(1)
	if '-p' in sys.argv:
		try:
			for i in range(len(sys.argv)):
				if sys.argv[i]=='-p':
					port=sys.argv[i+1]
					port=int(port)
					ping('127.0.0.1',port)
					print("Selected port:",str(port))
		except:
			print("\nDawn! An error occurred while selecting port.\n Using standard port: 80")
			port=80
	else:
		port=80
	if '-w' in sys.argv:
		try:
			for i in range(len(sys.argv)):
				if sys.argv[i]=='-w':
					filename=sys.argv[i+1]
					print("Output file:", filename)
		except:
			print("\nDawn! An error occurred while selecting archive.\n")
			filename=1
	else:
		filename=1
	global signal
	signal=True
	responses=[]
	wait=0.002
	t_server=Thread(target=listen, args=[responses])
	t_server.start()
	t_ping=Thread(target=rotate, args=[ipnetwork,port,filename,wait,responses])
	t_ping.start()
main()
