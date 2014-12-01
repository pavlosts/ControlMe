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
flag = 0


try:
    sock.bind((host, port))
except socket.error:
    print('Error binding socket...')
    time.sleep(10)
    sys.exit()

print("Socket has been bound!")

sock.listen(10)
print("Socket is now listening for connections!")

while 1:
    time.sleep(10)
    conn, addr = sock.accept()  # conn is name of the new socket

    print("Server is now connected with ", addr[0], " : ", str(addr[1]))

    while flag is 0:
        reply = conn.recv(4096)
        reply = reply.decode('utf-8')

        data = b"OK!"
        conn.sendall(data)

        print(reply)
        if reply in 'exit':
            flag = 1

        if flag is 1:
            print("Connection with ", addr[0], " is closing...")
            time.sleep(2)
            print("Bye!")
            conn.close()

    print("Do you want to close server?")
    ans = input()
    if ans == 'yes' or ans == 'Yes' or ans == 'YES' or ans == 'y' or ans == 'Y':
        print("Server is closing...")
        time.sleep(2)
        break



sock.close()
