import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hostname=socket.gethostname()
ipaddr=str(socket.gethostbyname(hostname))
sock.sendto(ipaddr.encode(),(socket.gethostname(),9876))
print("ip sent successfully")