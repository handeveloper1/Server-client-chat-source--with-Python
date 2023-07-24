import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Client'ten gelen yanıt: {data}")
            response = input("Mesajınızı Giriniz: ")
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"HATA: {e}")
            break
    client_socket.close()

def start_server():
    server_ip = '0.0.0.0'  # Tüm ağ arayüzlerini dinle
    server_port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)

    print(f"Server başlatıldı. Dinlenen IP: {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server.accept()
        print(f"Bağlantı Kabul Edildi {client_address[0]}:{client_address[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
