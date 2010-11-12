import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 5000))
s.listen(1)

c, addr = s.accept()
while 1:
    buf = c.recv(1024)
    val = sum(map(int, buf.split('+')))
    c.send(str(val) + '\n')
