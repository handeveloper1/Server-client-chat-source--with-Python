import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Bağlantı alındı: {client_address[0]}:{client_address[1]}")

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"Gelen mesaj ({client_address[0]}:{client_address[1]}): {data}")

        response = "Mesaj alındı: " + data
        client_socket.send(response.encode('utf-8'))

    client_socket.close()
    print(f"Bağlantı kapatıldı: {client_address[0]}:{client_address[1]}")

def start_server():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"Server başlatıldı. Dinlenen IP: {server_ip}, Port: {server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
