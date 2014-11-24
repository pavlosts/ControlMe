
import socket  # Necessary for sockets
import sys  # Necessary for "exit"

try:
    # Creates a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket...')

print('Socket created!')

