import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 5605
client_socket.connect(('127.0.0.1',port))
while True :
    message=input("enter your message: ")
    client_socket.send(bytes(message,'utf-8'))
    server_msg=client_socket.recv(1024)
    print(server_msg.decode('utf-8'))
    if message=="CLOSE SOCKET":
        client_socket.close()
        break