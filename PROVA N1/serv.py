import socket

CHUNK_SIZE = 4096
net = r'videos\Netflixbnt.png'
filme1 = r"videos\Filme1.mp4"
filme2 = r"videos\Filme2.mp4"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
server.bind(('192.168.1.4', 1234))
server.listen(1)
print("Server Iniciado")

def enviar_net(client):
    with open(net, 'rb') as f:
        while (chunk := f.read(CHUNK_SIZE)):
            client.send(chunk)
    client.shutdown(socket.SHUT_WR) 
def enviar_film1(client):
    with open(filme1, 'rb') as f:
        while (chunk := f.read(CHUNK_SIZE)):
            client.send(chunk)
    client.shutdown(socket.SHUT_WR)
def enviar_film2(client):
    with open(filme2, 'rb') as f:
        while (chunk := f.read(CHUNK_SIZE)):
            client.send(chunk)
    client.shutdown(socket.SHUT_WR)
while True:
    client, address = server.accept()
    print(f"Conexão de {address}")
    enviar_net(client)
    print("net.png enviado com sucesso!")
    client.close()
    client, address = server.accept()
    enviar_film1(client)
    print("filme1.mp4 enviado com sucesso!")
    client.close()
    client, address = server.accept()
    enviar_film2(client)
    print("filme2.mp4 enviado com sucesso!")
    client.close()
