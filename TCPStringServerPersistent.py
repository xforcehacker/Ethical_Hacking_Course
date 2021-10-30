from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The TCP server is ready.")

while True:
    connectionSocket, addr = serverSocket.accept()
    #INNER LOOP
    while True:    
        requestString = connectionSocket.recv(1024).decode()
        
        if requestString == 'Quit':
            print('connection is closed..')
            connectionSocket.close()
            #BREK INNER LOOP
            break
        else:
            responseString = requestString.upper()
            connectionSocket.send(requestString.encode())
