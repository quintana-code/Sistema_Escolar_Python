import customtkinter as ctk
from PIL import Image
from vistas.login_maestro import abrir_login_maestro
from vistas.login_Admin import abrir_login_admin
# CONFIGURACIÓN
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# VENTANA
ventana = ctk.CTk()
ventana.geometry("600x700")
ventana.title("Sistema Escolar")
ventana.resizable(False, False)

# FONDO GRIS
ventana.configure(fg_color="#E5E5E5")

# SOMBRA
sombra = ctk.CTkFrame(
    ventana,
    width=500,
    height=600,
    fg_color="#D0D0D0",
    corner_radius=25
)
sombra.place(relx=0.505, rely=0.505, anchor="center")

# TARJETA PRINCIPAL
card = ctk.CTkFrame(
    ventana,
    width=500,
    height=600,
    fg_color="white",
    corner_radius=25
)
card.place(relx=0.5, rely=0.5, anchor="center")

# LOGO
imagen = ctk.CTkImage(
    light_image=Image.open("vistas/imagenes/ardillapoo.png"),
    size=(80, 80)
)

logo = ctk.CTkLabel(
    card,
    image=imagen,
    text=""
)
logo.place(relx=0.5, y=70, anchor="center")

# TITULO
titulo = ctk.CTkLabel(
    card,
    text="Sistema Escolar",
    font=("Arial", 32, "bold"),
    text_color="#163B65"
)
titulo.place(relx=0.5, y=145, anchor="center")

# SUBTITULO
subtitulo = ctk.CTkLabel(
    card,
    text="Control de asistencia y gestión",
    font=("Arial", 16),
    text_color="gray"
)
subtitulo.place(relx=0.5, y=185, anchor="center")

# TEXTO PERFIL
perfil = ctk.CTkLabel(
    card,
    text="Selecciona tu perfil",
    font=("Arial", 24, "bold"),
    text_color="#163B65"
)
perfil.place(relx=0.5, y=280, anchor="center")

# DESCRIPCIÓN
descripcion = ctk.CTkLabel(
    card,
    text="Elige cómo deseas ingresar al sistema",
    font=("Arial", 14),
    text_color="gray"
)
descripcion.place(relx=0.5, y=315, anchor="center")

# FUNCIONES
def profesor():
    ventana.destroy()
    abrir_login_maestro()

def administrador():
    ventana.destroy()
    abrir_login_admin()

# BOTÓN PROFESOR
btn_profesor = ctk.CTkButton(
    card,
    text="PROFESOR \nTomar asistencia y consultar reportes",
    width=330,
    height=80,
    fg_color="#F5F7FB",
    text_color="#163B65",
    hover_color="#E6ECF5",
    corner_radius=15,
    command=profesor
)
btn_profesor.place(relx=0.5, y=410, anchor="center")

# BOTÓN ADMINISTRADOR
btn_admin = ctk.CTkButton(
    card,
    text="ADMINISTRADOR \nGestión de datos y control total",
    width=330,
    height=80,
    fg_color="#F5F7FB",
    text_color="#163B65",
    hover_color="#E6ECF5",
    corner_radius=15,
    command=administrador
)
btn_admin.place(relx=0.5, y=520, anchor="center")

# EJECUTAR
ventana.mainloop()