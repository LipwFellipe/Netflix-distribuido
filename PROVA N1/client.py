import socket
import os
import customtkinter as ctk

ip = '192.168.1.4'
port = 1234
saidanet, outputvid1, outputvid2 = "net.png", "filme1.mp4", "filme2.mp4"  # Nome dos arquivos OUTPUT
CHUNK_SIZE = 4096

def baixar_arquivo(nome_arquivo, output_path):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((ip, port))
            client.send(nome_arquivo.encode("utf-8"))  # Envia o nome do arquivo
            with open(output_path, 'wb') as f:
                while (chunk := client.recv(CHUNK_SIZE)):
                    f.write(chunk)
        print(f"Download concluído: {output_path}")
    except Exception as e:
        print(f"Erro ao baixar {nome_arquivo}: {e}")

def main():  # Função principal que ordena os downloads
    print(f"Conectando ao servidor {ip}:{port}")
    baixar_arquivo("net.png", saidanet)
    baixar_arquivo("filme1.mp4", outputvid1)
    baixar_arquivo("filme2.mp4", outputvid2)
    Interface()

def Interface(): # Interface Custom Tkinter
    root_tk= ctk.CTk()
    ctk.set_appearance_mode("dark")
    root_tk.geometry("400x370")
    root_tk.title("Seletor de filmes")
    root_tk.resizable(False, False)

    # Seção num1
    titulo_label = ctk.CTkLabel(root_tk, text="Seleção de filmes", font=("Helvetica", 24, "bold"))
    titulo_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
    button = ctk.CTkButton(root_tk, text="FILME 1: MODERN TIMES(1936)", fg_color="#821D1A", hover_color="#3A3A3A", command=lambda: videoP("filme1.mp4"))
    button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
    root_tk.grid_columnconfigure(0, weight=1)
    checklike = ctk.CTkCheckBox(root_tk, text="Gostou do filme?", fg_color="#821D1A", hover_color="#3A3A3A", onvalue=True, command=lambda: like_server(checklike, 1))
    checklike.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
    # Seção num2 
    button2 = ctk.CTkButton(root_tk, text="FIME 2 : O ESPAÇO SIDERAL", fg_color="#821D1A", hover_color="#3A3A3A", command=lambda: videoP("filme2.mp4"))
    button2.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
    checklike2 = ctk.CTkCheckBox(root_tk, text="Gostou do filme?", fg_color="#821D1A", hover_color="#3A3A3A", onvalue=True, command=lambda: like_server(checklike2, 2))
    checklike2.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="w")
    # Imagem
    from PIL import Image
    my_image = ctk.CTkImage(dark_image=Image.open("net.png"),size=(100, 100))
    image_label = ctk.CTkLabel(root_tk, image=my_image, text="")  # Mostra a imagem net.png
    image_label.place(x = 140, y = 250)
    root_tk.mainloop()

def like_server(check_gostado, num):
    if check_gostado.get():  # Se marcado, desativar para impedir alterações
        check_gostado.configure(state="disabled")
        mensagem = f"Cliente gostou do {num}º vídeo!"
        enviar_mensagem(mensagem)

def enviar_mensagem(mensagem):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((ip, port))
            client.send(mensagem.encode("utf-8"))
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def videoP(caminho_video):
    try:
        os.startfile(caminho_video)  # Abre o arquivo no aplicativo padrão
    except Exception as e:
        print(f"Erro ao abrir o vídeo: {e}")

if __name__ == "__main__":
    main()
