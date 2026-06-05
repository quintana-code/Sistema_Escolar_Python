import customtkinter as ctk
from Controladores.usuario_controlador import Controlador_Usuario
from vistas.menu_maestro import abrir_menu_maestro
from PIL import Image

def abrir_login_maestro():
    # ==========================
    # CONFIGURACIÓN
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    # ==========================
    # VENTANA
    ventana = ctk.CTk()
    ventana.geometry("600x700")
    ventana.title("Sistema Escolar")
    ventana.resizable(False, False)

    # ==========================
    # Fondo gris
    ventana.configure(fg_color="#E5E5E5")

    # ==========================
    # SOMBRA
    sombra = ctk.CTkFrame(
        ventana,
        width=420,
        height=620,
        corner_radius=20,
        fg_color="#CFCFCF"
    )
    sombra.place(relx=0.505, rely=0.505, anchor="center")

    # ==========================
    # FRAME PRINCIPAL
    frame = ctk.CTkFrame(
        ventana,
        width=420,
        height=620,
        corner_radius=20,
        fg_color="white"
    )
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # ==========================
    # BARRA SUPERIOR
    barra = ctk.CTkFrame(
        frame,
        width=320,
        height=50,
        fg_color="#163B65",
        corner_radius=20
    )
    barra.place(x=50, y=20)

    titulo = ctk.CTkLabel(
        barra,
        text="Sistema Escolar",
        font=("Arial", 20, "bold"),
        text_color="white"
    )
    titulo.place(x=20, y=2)

    subtitulo = ctk.CTkLabel(
        barra,
        text="Control de asistencias",
        font=("Arial", 12),
        text_color="#D6D6D6"
    )
    subtitulo.place(x=20, y=25)

    # ==========================
    # IMAGEN
    imagen = ctk.CTkImage(
        light_image=Image.open("vistas/imagenes/maestro.jpg"),
        size=(100, 100)
    )

    label_imagen = ctk.CTkLabel(
        frame,
        image=imagen,
        text=""
    )
    label_imagen.place(x=160, y=90)

    # ==========================
    #BIENVENIDA
    bienvenido = ctk.CTkLabel(
        frame,
        text="Bienvenido",
        font=("Arial", 30, "bold"),
        text_color="#222"
    )
    bienvenido.place(x=120, y=210)

    texto = ctk.CTkLabel(
        frame,
        text="Inicia sesión como maestro",
        font=("Arial", 13),
        text_color="gray"
    )
    texto.place(x=120, y=250)

    # ==========================
    # USUARIO
    lbl_usuario = ctk.CTkLabel(
        frame,
        text="USUARIO",
        font=("Arial", 12, "bold"),
        text_color="gray"
    )
    lbl_usuario.place(x=50, y=300)

    entry_usuario = ctk.CTkEntry(
        frame,
        width=320,
        height=45,
        placeholder_text="Nombre de usuario",
        corner_radius=10
    )
    entry_usuario.place(x=50, y=330)

    # ==========================
    # CONTRASEÑA
    lbl_password = ctk.CTkLabel(
        frame,
        text="CONTRASEÑA",
        font=("Arial", 12, "bold"),
        text_color="gray"
    )
    lbl_password.place(x=50, y=390)

    entry_password = ctk.CTkEntry(
        frame,
        width=320,
        height=45,
        placeholder_text="Contraseña",
        show="*",
        corner_radius=10
    )
    entry_password.place(x=50, y=420)

    # ==========================
    # FUNCION LOGIN
    def login():
        usuario = entry_usuario.get()
        password = entry_password.get()
        
        datos = Controlador_Usuario.login(usuario, password)
        
        print(datos)

        if datos:
            id_usuario = datos[0]
            nombre_usuario = datos[1]
            rol= datos[3]

            if rol.lower() in ["maestro", "docente"]:

                resultado.configure(
                    text="Inicio de sesión correcto",text_color="green")
                
                # retrasa la apertura de la nueva pantalla 'main menu' del maestro
                ventana.after(1000,lambda: 
                            (ventana.destroy(),abrir_menu_maestro(id_usuario,nombre_usuario, rol)
                    )
                )
            else:
                #validar si el usuario pertenece a la clase maestro o admin
                resultado.configure(
                    text="El suario NO es un maestro.", text_color="red"
                )
        else:
            #validar si la contraseña o usuario es incorrecta
            resultado.configure(
                text="Usuario o contraseña incorrectos", text_color="red"
            )

    # ==========================
    # BOTÓN
    boton = ctk.CTkButton(
        frame,
        text="Iniciar sesión",
        width=320,
        height=45,
        corner_radius=10,
        fg_color="#163B65",
        hover_color="#0D2B4D",
        command=login
    )
    boton.place(x=50, y=500)

    # ==========================
    # RESULTADO
    resultado = ctk.CTkLabel(
        frame,
        text="",
        font=("Arial", 12)
    )
    resultado.place(x=110, y=470)

    # ==========================
    # EJECUTAR
    ventana.mainloop()