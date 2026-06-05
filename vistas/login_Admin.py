from Controladores.usuario_controlador import Controlador_Usuario
from vistas.menu_admin import abrir_menu_admin
import customtkinter as ctk
from PIL import Image

def abrir_login_admin():
    # ==========================
    # CONFIGURACIÓN
    # ==========================
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    ventana = ctk.CTk()
    ventana.geometry("600x700")
    ventana.title("Sistema Escolar")
    ventana.resizable(False, False)
    ventana.configure(fg_color="#ececec")

    # ==========================
    # SOMBRA
    # ==========================
    sombra2 = ctk.CTkFrame(
        ventana,
        width=432,
        height=572,
        corner_radius=22,
        fg_color="#e8e8e8"
    )
    sombra2.place(relx=0.5, rely=0.5, anchor="center", x=8, y=8)

    sombra1 = ctk.CTkFrame(
        ventana,
        width=426,
        height=566,
        corner_radius=21,
        fg_color="#dcdcdc"
    )
    sombra1.place(relx=0.5, rely=0.5, anchor="center", x=4, y=4)

    # ==========================
    # FRAME PRINCIPAL (CENTRADO)
    # ==========================
    frame = ctk.CTkFrame(
        ventana,
        width=420,
        height=560,
        corner_radius=20,
        fg_color="white"
    )
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # ==========================
    # BARRA SUPERIOR
    # ==========================
    barra = ctk.CTkFrame(
        frame,
        width=420,
        height=55,
        fg_color="#163B65",
        corner_radius=20
    )
    barra.place(x=0, y=0)

    titulo = ctk.CTkLabel(
        barra,
        text="Sistema Escolar",
        font=("Arial", 20, "bold"),
        text_color="white"
    )
    titulo.place(x=20, y=5)

    subtitulo = ctk.CTkLabel(
        barra,
        text="Control de asistencias",
        font=("Arial", 12),
        text_color="#d6d6d6"
    )
    subtitulo.place(x=20, y=28)

    # ==========================
    # IMAGEN (CENTRADA)
    # ==========================
    imagen = ctk.CTkImage(
        light_image=Image.open("vistas/imagenes/admin.jpg"),
        size=(120, 100)
    )

    label_imagen = ctk.CTkLabel(frame, image=imagen, text="")
    label_imagen.place(relx=0.5, y=80, anchor="n")

    # ==========================
    # TEXTOS CENTRADOS
    # ==========================
    bienvenido = ctk.CTkLabel(
        frame,
        text="Bienvenido",
        font=("Arial", 30, "bold"),
        text_color="#222"
    )
    bienvenido.place(relx=0.5, y=190, anchor="n")

    texto = ctk.CTkLabel(
        frame,
        text="Inicia sesión como Administrador",
        font=("Arial", 13),
        text_color="gray"
    )
    texto.place(relx=0.5, y=235, anchor="n")

    # ==========================
    # USUARIO
    # ==========================
    lbl_usuario = ctk.CTkLabel(
        frame,
        text="USUARIO",
        font=("Arial", 12, "bold"),
        text_color="gray"
    )
    lbl_usuario.place(x=80, y=270)

    entry_usuario = ctk.CTkEntry(
        frame,
        width=260,
        height=40,
        placeholder_text="Nombre de usuario",
        corner_radius=10
    )
    entry_usuario.place(relx=0.5, y=300, anchor="n")

    # ==========================
    # CONTRASEÑA
    # ==========================
    lbl_password = ctk.CTkLabel(
        frame,
        text="CONTRASEÑA",
        font=("Arial", 12, "bold"),
        text_color="gray"
    )
    lbl_password.place(x=80, y=355)

    entry_password = ctk.CTkEntry(
        frame,
        width=260,
        height=40,
        placeholder_text="Contraseña",
        show="*",
        corner_radius=10
    )
    entry_password.place(relx=0.5, y=385, anchor="n")
    
    # ==========================
    # LOGIN
    # ==========================
    def login():
        usuario = entry_usuario.get()
        password = entry_password.get()

        datos = Controlador_Usuario.login(usuario, password)
        print(datos)

        if datos:
            id_usuario = datos[0]   
            nombre_usuario = datos[1]
            rol = datos[3]
            
            if rol.lower() in ["admin", "administrador"]:
                resultado.configure(text="Inicio de sesión correcto", text_color="green")
               
                #destruye esta ventana pero envia el id, el nombre y el rol al menu admin
                ventana.after(
                    1000,
                    lambda: (
                        ventana.destroy(),
                        abrir_menu_admin(id_usuario, nombre_usuario, rol)
                    )
                )
            else:
                resultado.configure(text="El usuario NO es administrador.", text_color="red")
        else:
            resultado.configure(
                text="Usuario o contraseña incorrectos",text_color="red")
    
    
    # ==========================
    # RESULTADO
    # ==========================
    resultado = ctk.CTkLabel(frame,text="",font=("Arial", 12))
    resultado.place(relx=0.5,y=450,anchor="n")

    # ==========================
    # BOTÓN
    # ==========================
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
    boton.place(relx=0.5, y=480, anchor="n")

    # ==========================
    # EJECUTAR
    # ==========================
    ventana.mainloop()