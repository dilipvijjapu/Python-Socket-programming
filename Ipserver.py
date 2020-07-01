

import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((socket.gethostname(),9876))

print("waiting for client")
while True:
    conn,addr=sock.recvfrom(2048)
    print("client ip address is:"+conn.decode())
    print("server exiting")
    sock.sendto("Thanks".encode(),(socket.gethostname(),9876))
    break
sock.close()


