import socket

def start_client():
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        message = input("Mesajınızı girin (Çıkmak için 'exit' yazın): ")
        if message.lower() == 'exit':
            break

        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print("Server'dan gelen yanıt:", response)

    client_socket.close()

if __name__ == "__main__":
    start_client()
