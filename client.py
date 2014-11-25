import socket  # Necessary for sockets
import sys  # Necessary for "exit"

try:
    # Creates a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket...')
    sys.exit()

print('Socket created!')

host = 'localhost'
port = 80

try:
    server = socket.gethostbyname(host)
except socket.gaierror:
    print('Error resolving hostname...')
    sys.exit()

try:
    # Connects to remote server
     res = sock.connect_ex((server, port))
except res is not 0:
    print('Error connection to server')
    sys.exit()

print('You are now connected to server: ', host, ' with IP ', server)

# Inform server that client is connected
msg = b"Client is now connected."

try:
    sock.sendall(msg)
except socket.error:
    print('Failed to send message to server')
    sys.exit()

print('Server knows client is connected')

# Recieve data from server
reply = sock.recv(4096)

print(reply)

sock.close()


