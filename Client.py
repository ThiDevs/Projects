import socket

while(True):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = "192.168.1.12"

    port = 9999

    # connection to hostname on the port.
    s.connect((host, port))

    # Receive no more than 1024 bytes
    msg = s.recv(1024)

    print (msg.decode('ascii'))

    s.close()
    time.sleep(2)