import socket
SERVERNAME = 'localhost'
PORT = 5000
while (True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try: 
            sendMessage = input("Enter message: (Enter 'quit' or 'QUIT' to disconnect from server: ")
            s.connect((SERVERNAME, PORT))
            s.send(sendMessage.encode())
            response_received = s.recv(1024)
            print(response_received.decode())
            #ADDING LOGIC TO DISCONNECT
            if ((sendMessage == 'quit') or (sendMessage == 'QUIT')):
                print ("Client has been disconnected")
                s.close()
                break
        #HANDLING ERROR
        except KeyboardInterrupt:
            print ("\n\nProgram terminated by user")
            s.close()
            break
