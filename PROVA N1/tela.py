import cv2
import customtkinter as ctk

def Interface():
    root_tk= ctk.CTk()
    ctk.set_appearance_mode("dark")
    root_tk.geometry("400x370")
    root_tk.title("Seletor de filmes")
    # Seção num1
    titulo_label = ctk.CTkLabel(root_tk, text="Seleção de filmes", font=("Helvetica", 24, "bold"))
    titulo_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
    button = ctk.CTkButton(root_tk, text="FILME 1: A AVENTURA DE RICK", fg_color="#821D1A", hover_color="#3A3A3A", command=video)
    button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
    root_tk.grid_columnconfigure(0, weight=1)
    check = ctk.CTkCheckBox(root_tk, text="Assistido?", fg_color="#821D1A", hover_color="#3A3A3A", command="" )
    check.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
    checkbox = ctk.CTkCheckBox(root_tk, text="Gostou do filme?", fg_color="#821D1A", hover_color="#3A3A3A", command="")
    checkbox.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")
    # Seção num2 
    button2 = ctk.CTkButton(root_tk, text="FIME 2 : O ESPAÇO SIDERAL", fg_color="#821D1A", hover_color="#3A3A3A", command=video1)
    button2.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
    checkbox_1 = ctk.CTkCheckBox(root_tk, text="Assistido?", fg_color="#821D1A", hover_color="#3A3A3A", command="")
    checkbox_1.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="w")
    checkbox_2 = ctk.CTkCheckBox(root_tk, text="Gostou do filme?", fg_color="#821D1A", hover_color="#3A3A3A", command="")
    checkbox_2.grid(row=4, column=1, padx=20, pady=(0, 20), sticky="w")
    # Imagem
    from PIL import Image
    my_image = ctk.CTkImage(dark_image=Image.open(r"D:\git\videos\Netflixbnt.png"),size=(100, 100))
    image_label = ctk.CTkLabel(root_tk, image=my_image, text="")  # display image with a CTkLabel
    image_label.place(x = 140, y = 250)
    root_tk.mainloop()

def video():
    video = cv2.VideoCapture(r"D:\git\videos\Filme1.mp4")
    if video.isOpened():
       validation, frame = video.read()
        # printar na tela no server q abriu
       while validation: 
           validation, frame = video.read()
           cv2.imshow("Filme", frame)
           key = cv2.waitKey(29) # Faz o loop metralhadora amenizar o intervalo de fotos por miliseg, ele consegue detectar uma tecla para fechar o programa
           if key == 27: #ESC
               cv2.destroyAllWindows()
               break
def video1():
    video = cv2.VideoCapture(r"D:\git\videos\Filme7.mp4")
    if video.isOpened():
       validation, frame = video.read()
        # printar na tela no server q abriu
       while validation: 
           validation, frame = video.read()
           cv2.imshow("Filme", frame)
           key = cv2.waitKey(30) # Faz o loop metralhadora amenizar o intervalo de fotos por miliseg, ele consegue detectar uma tecla para fechar o programa
           if key == 27: #ESC
               cv2.destroyAllWindows()
               break


Interface()

