import customtkinter as ctk
from PIL import Image

# CONFIGURACION DE VENTANA
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.geometry("600x700")
ventana.title("Sistema Escolar")
ventana.resizable(False, False)

# COLOR DE FONDO 
ventana.configure(fg_color="#ffffff")

# FRAME PRINCIPAL
frame = ctk.CTkFrame(
    ventana,
    width=320,
    height=560,
    corner_radius=20,
    fg_color="white"
)

frame.place(relx=0.5, rely=0.5, anchor="center")

# BARRA SUPERIOR
barra = ctk.CTkFrame(
    frame,
    width=320,
    height=50,
    fg_color="#163B65",
    corner_radius=20
)

barra.place(x=0, y=0) #muevo barra azul ala derecha si cambio x y y hacia

titulo = ctk.CTkLabel(
    barra,
    text="Sistema Escolar",
    font=("Arial", 20, "bold"),
    text_color="white"
)

titulo.place(x=20, y=0)

subtitulo = ctk.CTkLabel(
    barra,
    text="Control de asistencias",
    font=("Arial", 12),
    text_color="#d6d6d6"
)

subtitulo.place(x=20, y=24)

# TEXTO BIENVENIDA
bienvenido = ctk.CTkLabel(
    frame,
    text="Bienvenido",
    font=("Arial", 24, "bold"),
    text_color="#222"
)

bienvenido.place(x=85, y=150)

texto = ctk.CTkLabel(
    frame,
    text="Inicia sesión como Administrador ",
    font=("Arial", 13),
    text_color="gray"
)

texto.place(x=65, y=185)

# LABEL USUARIO
lbl_usuario = ctk.CTkLabel(
    frame,
    text="USUARIO",
    font=("Arial", 12, "bold"),
    text_color="gray"
)

lbl_usuario.place(x=30, y=230)

# ENTRY USUARIO
entry_usuario = ctk.CTkEntry(
    frame,
    width=260,
    height=40,
    placeholder_text="Nombre de usuario",
    corner_radius=10
)

entry_usuario.place(x=30, y=255)

# LABEL CONTRASEÑA
lbl_password = ctk.CTkLabel(
    frame,
    text="CONTRASEÑA",
    font=("Arial", 12, "bold"),
    text_color="gray"
)

lbl_password.place(x=30, y=320)

# ENTRY PASSWORD
entry_password = ctk.CTkEntry(
    frame,
    width=260,
    height=40,
    placeholder_text="Contraseña",
    show="*",
    corner_radius=10
)

entry_password.place(x=30, y=345)

# FUNCION LOGIN inicio de sesion
def login():
    usuario = entry_usuario.get()
    password = entry_password.get()

    if usuario == "admin" and password == "1234":
        resultado.configure(
            text="Inicio de sesión correcto",
            text_color="green"
        )
    else:
        resultado.configure(
            text="Usuario o contraseña incorrectos",
            text_color="red"
        )

# BOTON
boton = ctk.CTkButton(
    frame,
    text="Iniciar sesión",
    width=260,
    height=45,
    corner_radius=10,
    fg_color="#163B65",
    hover_color="#0d2b4d",
    command=login
)

boton.place(x=30, y=420)

# RESULTADO
resultado = ctk.CTkLabel(
    frame,
    text="",
    font=("Arial", 12)
)

resultado.place(x=80, y=390)

# logo del login
imagen = ctk.CTkImage(
    light_image=Image.open("imagenes/admin.jpg"),
    size=(150, 100)
)

label_imagen = ctk.CTkLabel(
    frame,
    image= imagen, text= ""
    
)

label_imagen.place(x=70, y=50)

# EJECUTAR
ventana.mainloop()