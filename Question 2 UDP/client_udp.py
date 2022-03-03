import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 2345

filename = 'udp_server.txt'
s.sendto(filename.encode(), (host,port))

f = open('udp_client.txt','r')
data = f.read(1024)
s.sendto(data.encode(), (host, port))

reply, addr = s.recvfrom(1024)
print("Server reply:",reply.decode())

s.close()
f.close()