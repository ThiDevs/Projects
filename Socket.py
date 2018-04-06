import socket

# create a socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
print(socket.gethostbyname(socket.gethostname()))

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)
i = 0
while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    msg = 'Thank you for connecting '+ str(i) + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    i += 1

clientsocket.close()

print("Sai")