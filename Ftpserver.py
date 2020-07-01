import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(4)
print("waiting for connection")
while True:
    conn,addr=s.accept()
    print("successfully connected to",addr)
    dat=conn.recv(2048)
    print("server recieved:",dat.decode())
    file=open("input.txt",'rb')
    rd=file.read(1024)
    while rd:
        conn.send(rd)
        print("sent",rd)
        rd=file.read(1024)
    file.close()
    print("file successfully sent")
    conn.close()
