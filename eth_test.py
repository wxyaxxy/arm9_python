#! /usr/bin/python3
import socket

s = socket.socket()
# print(socket.getaddrinfo())
host = socket.gethostname()
port = 1235
ip = socket.gethostbyname("wangbo")
print(host)
print(ip)
# s.bind((host, port))
s.connect(('192.168.1.3', port))
# s.listen(5)
#

msg = s.recv(1024)

s.close()

print(msg)

while True:
    c, addr = s.accept()
    print(addr)
    s.send("欢迎")
    c.close()
