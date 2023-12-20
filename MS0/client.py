import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 5605
client_socket.connect((ip, port))

while True:
    message = input("Enter your message: ")

    client_socket.send(message.encode())

    if message == "CLOSE SOCKET":
        print("Closing connection with the server.")
        client_socket.close()
        break

    response = client_socket.recv(1024).decode()
    print("Server response:", response)