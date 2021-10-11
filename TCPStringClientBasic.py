from socket import *

serverName = 'localhost'
serverPort = 5000
requestString = input("Input a sentence: ")
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(requestString.encode())
response = clientSocket.recv(1024)
print(response.decode())
clientSocket.close()

