import socket
import threading

CHUNK_SIZE = 4096
files = {
    "net.png": r'videos\Netflixbnt.png',
    "filme1.mp4": r"videos\Filme1.mp4",
    "filme2.mp4": r"videos\Filme7.mp4"
}

def handle_client(client, address):
    print(f"Conexão de {address}")
    try:
        # Recebe o nome do arquivo solicitado
        request = client.recv(1024).decode("utf-8")
        if request == "Cliente gostou do 1º vídeo!":
            print("Cliente gostou do 1º vídeo!")
        elif request == "Cliente gostou do 2º vídeo!":
            print("Cliente gostou do 2º vídeo!")
        else:
            print(f"Arquivo solicitado: {request}")
            
            if request in files:
                enviar_arquivo(client, files[request])
                print(f"{request} enviado com sucesso!")
            else:
                client.send(b"Arquivo nao encontrado.")
                print(f"Arquivo {request} nao encontrado.")
    except Exception as e:
        print(f"Erro ao lidar com o cliente {address}: {e}")
    finally:
        client.close()

def enviar_arquivo(client, filepath):
    with open(filepath, 'rb') as f:
        while (chunk := f.read(CHUNK_SIZE)):
            client.send(chunk)
    client.shutdown(socket.SHUT_WR)

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    server.bind(('192.168.1.4', 1234))
    server.listen(5)  
    print("Servidor iniciado")

    while True:
        client, address = server.accept()
        # Cria uma nova thread para cada cliente
        client_thread = threading.Thread(target=handle_client, args=(client, address))
        client_thread.start()
