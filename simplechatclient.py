import socket
import time

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen()
print("waiting for connectiions")
conn, addr = s.accept()
print("client got connected")
time.sleep(3)

conn.send("welcome to server".encode())
while 1:
    msg = input(str(">>"))
    msg = msg.encode()
    conn.send(msg)
    print("message sent")
    msg2=conn.recv(1024)
    msg2=msg2.decode()
    print("client message:",msg2)
