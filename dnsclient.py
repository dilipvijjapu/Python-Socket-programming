"""import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect((socket.gethostname(),8888))
print("connecting to server")
while True:
    dat=input("Domain:" )
    if dat == 'bye' or not dat:
        break
    else:
        r.sendto(dat.encode(),(socket.gethostname(),8888))
        data=s.recv(1024)
        print("IP addresss of server is :",data.decode())
s.close()
r.close()"""
import socket
host = socket.gethostname()
sock_r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_r.bind((host, 9997))
print("Connecting...")
while True:
 data = input("Domain : ")
 if data == 'bye' or not data:
   break
 else:
   sock_s.sendto(data.encode(), (host, 9999))
   data = sock_r.recv(1024)
   print("IP: "+data.decode())
sock_s.close()
sock_r.close()