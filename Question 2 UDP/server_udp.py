import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 2345
s.bind((host, port))

while True:
    filename, addr = s.recvfrom(1024)
    filename = filename.decode()
    f = open(filename,'w')

    data, addr = s.recvfrom(1024)
    f.write(data.decode())

    print("Received a file from "+str(addr)+": "+filename)
    f.close()

    reply = 'File has been received!'
    s.sendto(reply.encode(), addr)