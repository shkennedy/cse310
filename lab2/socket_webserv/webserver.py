#!/usr/bin/python2.7.3
from socket import *                        

# Prepare a sever socket
serverPort = 6543
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True: 
    # Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()   
    try: 
        # Recieve request from client (filename)
        message = connectionSocket.recv(1024)
        filename = message.split()[1]                  
        f = open(filename[1:])                         
        outputdata = f.read()
        
        # Send one HTTP header line into socket 
        connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n') 

        # Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):            
            connectionSocket.send(outputdata[i]) 
        connectionSocket.close() 
    except IOError: 
        # Send response message for file not found
        message = 'HTTP/1.1 404 File Not Found\nContent-Type: text/html\n\n' 
        connectionSocket.send(message)
        
        # Close client socket
        connectionSocket.close()

    serverSocket.close()                                     
