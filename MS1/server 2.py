import socket
import threading

PORT = 5605
ADDR = ('127.0.0.1', PORT)

def threaded(conn, addr):
    print("[NEW CONNECTION] " + str(addr) + " connected.")
    
    while True:
        message = conn.recv(1024).decode('utf-8')
        if message == "CLOSE SOCKET":
            break

        response = message.upper()
        conn.sendall(response.encode('utf-8'))

    conn.close()
    
    print("[CONNECTION CLOSED] " + str(addr) + " disconnected.")
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 2}")

def main():
    print("Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    
    while True:
        conn, addr = server.accept()
        threading.Lock().acquire()
        threading.Thread(target=threaded, args=(conn, addr)).start()
        
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()

