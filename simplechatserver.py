import socket
s = socket.socket()
host=socket.gethostname()
port = 8080
s.connect((host,port))
print("connected to server")
while 1:
        msg = s.recv(1024)
        msg= msg.decode()
        print("Server:message",msg)
        newmsg=input(str("<<"))
        newmsg=newmsg.encode()
        s.send(newmsg)