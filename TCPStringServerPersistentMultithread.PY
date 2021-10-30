from socket import *
import threading

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is running...')

#SERVICE FUNCTION
def serv_func(conn_sock):
    while True:
        msg = conn_sock.recv(1024).decode()
        if msg == 'quit' or msg == 'Quit':
            conn_sock.close()
            break
        else:
            conn_sock.send(msg.upper().encode())

class ServiceThread(threading.Thread):
    def __init__(self, conn_sock):
        threading.Thread.__init__(self)
        self.conn_sock = conn_sock

    def run(self):
        serv_func(self.conn_sock)


while True:
    conn_sock, address = serverSocket.accept()
    new_thread = ServiceThread(conn_sock)
    #start thread
    new_thread.start()
