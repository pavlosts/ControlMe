import sys
import socket
import time

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create a socket...")
    sys.exit()

print("Socket created!")

host = ''
port = 8888

try:
    sock.bind((host, port))
except socket.error:
    print('Error binding socket...')
    sys.exit()

print("Socket has been bound!")

sock.listen(10)
print("Socket is now listening for connections!")

time.sleep(10)

conn, addr = sock.accept()  # conn is name of the new socket

print("Server is now connected with ", addr[0], " : ", str(addr[1]))

reply = conn.recv(4096)
print(reply.decode('utf-8'))

data = b"Hello client!"
conn.sendall(data)

print("Press ENTER to close the program.")
input()

conn.close()
sock.close()
