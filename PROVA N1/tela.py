import os
import customtkinter as ctk

def Interface():
    root_tk = ctk.CTk()
    ctk.set_appearance_mode("dark")
    root_tk.geometry("400x370")
    root_tk.title("Seletor de filmes")
    root_tk.resizable(False, False)

    # Seção num1
    titulo_label = ctk.CTkLabel(root_tk, text="Seleção de filmes", font=("Helvetica", 24, "bold"))
    titulo_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)

    button = ctk.CTkButton(root_tk, text="FILME 1: A AVENTURA DE RICK", fg_color="#821D1A", hover_color="#3A3A3A", command=lambda: abrir_video(r"D:\Projetos VSCODE\Server Netflix\videos\Filme1.mp4"))
    button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

    root_tk.grid_columnconfigure(0, weight=1)

    check_assistido = ctk.CTkCheckBox(root_tk, text="Assistido?", fg_color="#821D1A", hover_color="#3A3A3A", onvalue="assis", offvalue="nassis", command=lambda: Verificar(check_assistido))
    check_assistido.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")

    checkbox = ctk.CTkCheckBox(root_tk, text="Gostou do filme?", fg_color="#821D1A", hover_color="#3A3A3A", onvalue="sim", offvalue="não")
    checkbox.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")

    # Seção num2 
    button2 = ctk.CTkButton(root_tk, text="FILME 2: O ESPAÇO SIDERAL", fg_color="#821D1A", hover_color="#3A3A3A", command=lambda: abrir_video(r"D:\Projetos VSCODE\Server Netflix\videos\Filme2.mp4"))
    button2.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

    checkbox_1 = ctk.CTkCheckBox(root_tk, text="Assistido?", fg_color="#821D1A", hover_color="#3A3A3A", onvalue="sim", offvalue="não")
    checkbox_1.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="w")

    checkbox_2 = ctk.CTkCheckBox(root_tk, text="Gostou do filme?", fg_color="#821D1A", hover_color="#3A3A3A", onvalue="sim", offvalue="não")
    checkbox_2.grid(row=4, column=1, padx=20, pady=(0, 20), sticky="w")

    # Imagem
    from PIL import Image
    my_image = ctk.CTkImage(dark_image=Image.open(r"D:\Projetos VSCODE\Server Netflix\videos\Netflixbnt.png"), size=(100, 100))
    image_label = ctk.CTkLabel(root_tk, image=my_image, text="")
    image_label.place(x=140, y=250)

    root_tk.mainloop()

def Verificar(check_assistido):
    vl_check1 = check_assistido.get()
    if vl_check1 == "assis":
        print("ASSISTIDO!")
    else:
        print("NÃO ASSISTIDO!")

def abrir_video(caminho_video):
    try:
        os.startfile(caminho_video)  # Abre o arquivo no aplicativo padrão
    except Exception as e:
        print(f"Erro ao abrir o vídeo: {e}")

Interface()
