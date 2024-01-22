import socket

soc_obj=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
soc_obj2=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
print("Welcome")
host = '127.0.0.1'  # Use '' to bind to all available interfaces
port = 12345
t1=(host,port)
soc_obj.bind(t1)
soc_obj.listen(5)
soc_obj2.connect(t1)

conn,add=soc_obj.accept()
data=1001
conn.send(data.to_bytes(4,byteorder='big'))
print(soc_obj2.recv(1024))

soc_obj2.close()
soc_obj.close()