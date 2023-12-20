import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 5605
server_socket.bind((ip, port))

server_socket.listen(1)
print("Server is listening for connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Connected with client:", client_address)

    while True:
        message = client_socket.recv(1024).decode()

        if message == "CLOSE SOCKET":
            print("Closing connection with client:", client_address)
            client_socket.close()
            break

        response = message.upper()
        client_socket.send(response.encode())