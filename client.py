import socket  # Necessary for sockets
import sys  # Necessary for "exit"
import time

try:
    # Creates a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket...')
    sys.exit()

print('Socket created!')

ip = input('Enter IP or hostname')
port = 8888
flag = 0

try:
    server = socket.gethostbyname(ip)
except socket.gaierror:
    print('Error resolving hostname...')
    time.sleep(5)
    sys.exit()

try:
    # Connects to remote server
    res = sock.connect_ex((server, port))
except res is not 0:
    print('Error connection to server')
    time.sleep(10)
    sys.exit()

print('You are now connected to server: ', socket.getfqdn(ip), ' with IP ', ip)

while 1:

    msg = input()

    if msg in 'exit':
        flag = 1

    msg = msg.encode('utf-8')
    try:
        sock.sendall(msg)
    except socket.error:
        print('Failed to send message to server')
        time.sleep(10)
        sys.exit()

    # Receive data from server
    reply = sock.recv(4096)
    print(reply.decode('utf-8'))

    if flag is 1:
        print("Connection with ", ip, " is closing...")
        time.sleep(2)
        print("Bye!")
        break

sock.close()
time.sleep(2)
