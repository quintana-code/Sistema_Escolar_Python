import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x650")
app.title("Panel de administrador")
app.resizable(False, False)

# ======================
# ENCABEZADO CON SOMBRA
# ======================

shadow_header = ctk.CTkFrame(
    app,
    fg_color="#d9d9d9",
    corner_radius=15
)
shadow_header.pack(fill="x", padx=38, pady=(10, 0))

header = ctk.CTkFrame(
    shadow_header,
    fg_color="white",
    corner_radius=15
)
header.pack(fill="x", padx=2, pady=2)

titulo = ctk.CTkLabel(
    header,
    text="Panel de administrador",
    font=("Arial", 28, "bold")
)
titulo.pack(anchor="w", padx=25, pady=(12, 0))

subtitulo = ctk.CTkLabel(
    header,
    text="SUPERUSUARIO",
    text_color="gray"
)
subtitulo.pack(anchor="w", padx=25, pady=(0, 12))

# ======================
# ICONOS
# ======================

icono_admin = ctk.CTkImage(
    light_image=Image.open("iconos/adminicon.png"),
    dark_image=Image.open("iconos/adminicon.png"),
    size=(50, 50)
)

icono_usuario = ctk.CTkImage(
    light_image=Image.open("iconos/usuario.png"),
    dark_image=Image.open("iconos/usuario.png"),
    size=(28, 28)
)

icono_reportes = ctk.CTkImage(
    light_image=Image.open("iconos/reportes.png"),
    dark_image=Image.open("iconos/reportes.png"),
    size=(28, 28)
)

icono_salir = ctk.CTkImage(
    light_image=Image.open("iconos/salir.png"),
    dark_image=Image.open("iconos/salir.png"),
    size=(28, 28)
)

# ======================
# TARJETA DE BIENVENIDA
# ======================

frame_bienvenida = ctk.CTkFrame(
    app,
    fg_color="#143A5A",
    corner_radius=20,
    height=100
)
frame_bienvenida.pack(fill="x", padx=40, pady=15)

lbl_icono = ctk.CTkLabel(
    frame_bienvenida,
    image=icono_admin,
    text=""
)
lbl_icono.place(x=25, y=25)

lbl_hola = ctk.CTkLabel(
    frame_bienvenida,
    text="Hola, Administrador",
    font=("Arial", 22, "bold"),
    text_color="white"
)
lbl_hola.place(x=95, y=15)

lbl_desc = ctk.CTkLabel(
    frame_bienvenida,
    text="Tienes acceso total al sistema. Desde aquí puedes gestionar\n"
         "las entidades alumno  y consultar reportes.",
    text_color="white",
    justify="left"
)
lbl_desc.place(x=95, y=50)

# ======================
# GESTIÓN DE DATOS
# ======================

seccion1 = ctk.CTkLabel(
    app,
    text="GESTIÓN DE DATOS",
    font=("Arial", 14, "bold"),
    text_color="gray"
)
seccion1.pack(anchor="w", padx=40)

btn_alumnos = ctk.CTkButton(
    app,
    text="   Alumnos",
    image=icono_usuario,
    compound="left",
    anchor="w",
    height=60,
    fg_color="#F5F5F5",
    text_color="black",
    hover_color="#EAEAEA",
    corner_radius=12,
    font=("Arial", 16, "bold")
)
btn_alumnos.pack(fill="x", padx=40, pady=8)

# ======================
# CONSULTAS
# ======================

seccion2 = ctk.CTkLabel(
    app,
    text="CONSULTAS",
    font=("Arial", 14, "bold"),
    text_color="gray"
)
seccion2.pack(anchor="w", padx=40, pady=(10, 0))

btn_reportes = ctk.CTkButton(
    app,
    text="   Reportes",
    image=icono_reportes,
    compound="left",
    anchor="w",
    height=60,
    fg_color="#F5F5F5",
    text_color="black",
    hover_color="#EAEAEA",
    corner_radius=12,
    font=("Arial", 16, "bold")
)
btn_reportes.pack(fill="x", padx=40, pady=8)

# ======================
# SISTEMA
# ======================

seccion3 = ctk.CTkLabel(
    app,
    text="SISTEMA",
    font=("Arial", 14, "bold"),
    text_color="gray"
)
seccion3.pack(anchor="w", padx=40, pady=(10, 0))

btn_salir = ctk.CTkButton(
    app,
    text="   Cerrar sesión",
    image=icono_salir,
    compound="left",
    anchor="w",
    height=60,
    fg_color="#F5F5F5",
    text_color="black",
    hover_color="#EAEAEA",
    corner_radius=12,
    font=("Arial", 16, "bold")
)
btn_salir.pack(fill="x", padx=40, pady=8)

app.mainloop()