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
    print(res)
except res is not 0:
    print('Error connectin to server')

print('You are now connected to server: ', host, ' with IP ', server)


