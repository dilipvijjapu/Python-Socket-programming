import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),6987))
ms=s.recv(1024)
print("server: ",ms.decode())
while True:
           rr=input(str("<<"))
           rr=rr.encode()
           s.send(rr)
           rs=s.recv(1024)
           print("server :",rs.decode())
           rt=s.recv(1024)
           print("client1 <<",rt.decode())
s.close()