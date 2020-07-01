"""import socket
dns={
    'google':'172.13.31.89',
    'gmail':'154.32.176.11',
    'w3schools':'143.76.142.21',
    'yahoo':'162.54.26.11',
    'youtube':'136.38.31.11'
}
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((socket.gethostname(),8888))
print("waiting ofr client to connect")
while True:
    data,addr=s.recvfrom(1024)
    print("domain:"+data.decode(),addr)
    ip=" "
    if data.decode() in dns.keys():
        ip=dns.get(data.decode())
    elif(data.decode() == "bye") or not data:
        break
    else:
        ip="NOt found"
    r.sendto(ip.encode(),(socket.gethostname(),8888))
    s.close()
    r.close()"""

import socket
dns = {
 'google': '172.13.31.89',
 'gmail': '154.32.176.11',
 'w3school': '143.76.142.21',
 'yahoo': '162.54.26.11',
 'bing': '148.47.25.33',
 'youtube': '163.38.31.11'
 }
host = socket.gethostname()
sock_r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_r.bind((host,9999))
print("Waiting for client...")
while True:
 data, addr = sock_r.recvfrom(1024)
 print('Domain :'+data.decode(), addr)
 ip = ""
 if data.decode() in dns.keys():
  ip = dns.get(data.decode())
 elif( data.decode() == "bye" ) or not data:
    break
 else:
   ip = "Not Found"
sock_s.sendto(ip.encode(),(host,9997))
sock_r.close()
sock_s.close()