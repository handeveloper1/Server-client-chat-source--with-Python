import socket

def start_client():
    server_ip = 'SERVER_IP_ADDRESS'
    server_port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        try:
            message = input("Mesajınızı Giriniz: ")
            client.send(message.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            print(f"Server'dan gelen yanıt: {response}")
        except Exception as e:
            print(f"HATA: {e}")
            break

    client.close()

if __name__ == "__main__":
    start_client()
