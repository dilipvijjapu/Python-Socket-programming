import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
s.send("required client connected ".encode())
with open("output,txt",'wb') as file:
    print('file originated')
    while True:
        data=s.recv(1024)
        print("datarecieved",data.decode)
        if not data:
            break
        file.write(data)
    file.close()
    print("FTP protocol succesfully implemented using tcp protcols")
    s.close()