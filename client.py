import socket  # Necessary for sockets
import sys  # Necessary for "exit"

try:
    # Creates a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket...')
    sys.exit()

print('Socket created!')

print('Enter host\'s IP')
ip = input()
port = 8888

try:
    server = socket.gethostbyname(ip)
except socket.gaierror:
    print('Error resolving hostname...')
    sys.exit()

try:
    # Connects to remote server
    res = sock.connect_ex((server, port))
except res is not 0:
    print('Error connection to server')
    sys.exit()

print('You are now connected to server: ', socket.getfqdn(ip), ' with IP ', ip)

while 1:

    msg = input()
    if msg in 'exit':
        break

    msg = msg.encode('utf-8')

    try:
        sock.sendall(msg)
    except socket.error:
        print('Failed to send message to server')
        sys.exit()

    print('Server knows client is connected')

    # Receive data from server
    reply = sock.recv(4096)
    print(reply.decode('utf-8'))

sock.close()

print("Press ENTER to close program.")
input()
