import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
client.connect(('',8080))
message = "I am CLIENT\n"
client.sendto(message.encode(), ('',8080))
=======
client.connect(('192.168.2.1',8080))
message = "I am CLIENT\n"
client.sendto(message.encode(), ('192.168.2.1',8080))
>>>>>>> ba6a939cbcaf24bfa71b0834e99eb39740104bfc
data = client.recv(4096)
from_server = data.decode()
client.close()
print(from_server)
