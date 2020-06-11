#!/usr/bin/python3

import socket

# AF_INIT MEANS IT IS IPV4 AND SOCK_STREAM MEANS IT IS A TCP CONNECTION
serversocket = socket.socket(
socket.AF_INET, socket.SOCK_STREAM
)

#You can specify and port
host = socket.gethostname()  #get ip address, instead of it you can write down the machine ip that you are running the code on like '192.168.0.5'
port = 444

serversocket.bind((host, port))

#number specify how many request are allowed
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print("You Have Received Connection From %s " % str(address))

    message = 'Nice !!! You have been connected to the server' + "\r\n"

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
