import socket
import cv2
import customtkinter as ctk

ip = '192.168.1.4'
port = 1234 
saidanet, outputvid1, outputvid2 = "net.png", "filme1.mp4", "filme2.mp4"
CHUNK_SIZE = 4096

def img_net(ip, port): # Baixa a imagem da netflix 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
    client.connect((ip, port))
    with open(saidanet, 'wb') as f:
        while (chunk := client.recv(CHUNK_SIZE)):
            f.write(chunk)
def baixrvid1(ip, port): # Baixa o filme1
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
    client.connect((ip, port))
    with open(outputvid1, 'wb') as f:
        while (chunk := client.recv(CHUNK_SIZE)):
            f.write(chunk)
def baixrvid2(ip, port): # Baixa o filme2
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
    client.connect((ip, port))
    with open(outputvid2, 'wb') as f:
        while (chunk := client.recv(CHUNK_SIZE)):
            f.write(chunk)
def main(): # Função principal onde ordena para baixar arquivos e printa na tela
    print(f"Conectando ao servidor {ip}:{port}")
    img_net(ip, port)
    print(f"Download concluído: {saidanet}")
    baixrvid1(ip, port)
    print(f"Download concluído: {outputvid1}")
    baixrvid2(ip, port)
    print(f"Download concluído: {outputvid2}")
    Interface()
def Interface(): # Interface Custom Tkinter
    root_tk= ctk.CTk()
    ctk.set_appearance_mode("dark")
    root_tk.geometry("400x370")
    root_tk.title("Seletor de filmes")
    # Seção num1
    titulo_label = ctk.CTkLabel(root_tk, text="Seleção de filmes", font=("Helvetica", 24, "bold"))
    titulo_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
    button = ctk.CTkButton(root_tk, text="FILME 1: MODERN TIMES(1936)", fg_color="#821D1A", hover_color="#3A3A3A", command=videoP)
    button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
    root_tk.grid_columnconfigure(0, weight=1)
    check = ctk.CTkCheckBox(root_tk, text="Assistido?", fg_color="#821D1A", hover_color="#3A3A3A", command="")
    
    check.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
    checkbox = ctk.CTkCheckBox(root_tk, text="Gostou do filme?", fg_color="#821D1A", hover_color="#3A3A3A", command="")
    checkbox.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")
    # Seção num2 
    button2 = ctk.CTkButton(root_tk, text="FIME 2 : O ESPAÇO SIDERAL", fg_color="#821D1A", hover_color="#3A3A3A", command=videoS)
    button2.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
    checkbox_1 = ctk.CTkCheckBox(root_tk, text="Assistido?", fg_color="#821D1A", hover_color="#3A3A3A", command="")
    checkbox_1.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="w")
    checkbox_2 = ctk.CTkCheckBox(root_tk, text="Gostou do filme?", fg_color="#821D1A", hover_color="#3A3A3A", command="")
    checkbox_2.grid(row=4, column=1, padx=20, pady=(0, 20), sticky="w")
    # Imagem
    from PIL import Image
    my_image = ctk.CTkImage(dark_image=Image.open("net.png"),size=(100, 100))
    image_label = ctk.CTkLabel(root_tk, image=my_image, text="")  # display image with a CTkLabel
    image_label.place(x = 140, y = 250)
    root_tk.mainloop()
def videoP(): # Faz o filme prímario rodar
    film1 = cv2.VideoCapture("filme1.mp4")
    if film1.isOpened():
       validation, frame = film1.read()
       while validation: 
           validation, frame = film1.read()
           cv2.imshow("Filme", frame)
           key = cv2.waitKey(29) # Faz o loop metralhadora amenizar o intervalo de fotos por miliseg, ele consegue detectar uma tecla para fechar o programa
           if key == 27: #ESC
               cv2.destroyAllWindows()
               break
def videoS(): # Faz o filme secundario rodar
    film1 = cv2.VideoCapture("filme2.mp4")
    if film1.isOpened():
       validation, frame = film1.read()
       while validation: 
           validation, frame = film1.read()
           cv2.imshow("Filme", frame)
           key = cv2.waitKey(29) # Faz o loop metralhadora amenizar o intervalo de fotos por miliseg, ele consegue detectar uma tecla para fechar o programa
           if key == 27: #ESC
               cv2.destroyAllWindows()
               break

if __name__ == "__main__":
    main()
