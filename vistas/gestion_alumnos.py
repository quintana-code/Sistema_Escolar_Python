import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1200x700")
app.title("Gestión de alumnos")

# ==========================
# ENCABEZADO
# ==========================

titulo = ctk.CTkLabel(
    app,
    text="Gestión de alumnos",
    font=("Arial", 34, "bold"),
    text_color="#173B5B"
)
titulo.pack(anchor="w", padx=30, pady=(20, 0))

subtitulo = ctk.CTkLabel(
    app,
    text="BASE DE DATOS",
    font=("Arial", 14),
    text_color="gray"
)
subtitulo.pack(anchor="w", padx=35)
# ==========================
# BOTONES SUPERIORES
# ==========================

frame_superior = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
frame_superior.pack(fill="x", padx=30, pady=15)

btn_agregar = ctk.CTkButton(
    frame_superior,
    text="+ Agregar alumno",
    width=180,
    height=45,
    fg_color="#173B5B",
    hover_color="#102C45",
    corner_radius=25,
    font=("Arial", 14, "bold")
)

btn_agregar.pack(side="right")
# ==========================
# CONTENEDOR TABLA
# ==========================

frame_tabla = ctk.CTkFrame(
    app,
    fg_color="white",
    corner_radius=20,
    border_width=1,
    border_color="#E5E7EB"
)

frame_tabla.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)

# ==========================
# ENCABEZADO TABLA
# ==========================

header_frame = ctk.CTkFrame(
    frame_tabla,
    fg_color="transparent"
)

header_frame.pack(fill="x", padx=20, pady=(20, 10))

titulo_directorio = ctk.CTkLabel(
    header_frame,
    text="Directorio Activo",
    font=("Arial", 22, "bold"),
    text_color="#173B5B"
)

titulo_directorio.pack(side="left")

contador = ctk.CTkLabel(
    header_frame,
    text="10 registros",
    fg_color="#F3F4F6",
    corner_radius=15,
    padx=15,
    pady=5,
    text_color="gray"
)

contador.pack(side="right")

# ==========================
# ==========================
# TABLA CON SCROLL
# ==========================

scroll_tabla = ctk.CTkScrollableFrame(
    frame_tabla,
    fg_color="white"
)

scroll_tabla.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)

# ==========================
# ENCABEZADOS
# ==========================

encabezado = ctk.CTkFrame(
    scroll_tabla,
    fg_color="#F8FAFC",
    corner_radius=10
)

encabezado.pack(fill="x", pady=(0, 5))

ctk.CTkLabel(encabezado, text="ID", width=120, font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=10)
ctk.CTkLabel(encabezado, text="NOMBRE", width=350, font=("Arial", 12, "bold")).grid(row=0, column=1, padx=5)
ctk.CTkLabel(encabezado, text="MATRÍCULA", width=150, font=("Arial", 12, "bold")).grid(row=0, column=2, padx=5)
ctk.CTkLabel(encabezado, text="GRUPO", width=100, font=("Arial", 12, "bold")).grid(row=0, column=3, padx=5)
ctk.CTkLabel(encabezado, text="ACCIONES", width=250, font=("Arial", 12, "bold")).grid(row=0, column=4, padx=5)

# ==========================
# DATOS
# ==========================

datos = [
    ("n383w6nt", "Ana Martínez", "-", "3ro"),
    ("o10gq1q5", "Carlos Rodríguez", "-", "2do"),
    ("z7p9ekeu", "Diego Morales", "-", "1ro"),
    ("ey7k4dxf", "Elena Castillo", "-", "1ro"),
    ("dy1odvxf", "Juan García", "-", "1ro"),
    ("inmpe7x", "Laura Fernández", "-", "3ro"),
    ("5vrzfe04", "María López", "-", "1ro"),
    ("fdskhfye", "Miguel Herrera", "-", "3ro"),
    ("amrxmn14", "Pedro Sánchez", "-", "3ro"),
    ("xpqwe123", "Sofía Ramírez", "-", "2do"),
    ("extra01", "Alumno Extra", "-", "1ro"),
    ("extra02", "Alumno Extra", "-", "2do"),
    ("extra03", "Alumno Extra", "-", "3ro"),
    ("extra04", "Alumno Extra", "-", "1ro"),
    ("extra05", "Alumno Extra", "-", "2do"),
]

contador.configure(text=f"{len(datos)} registros")

for alumno in datos:

    fila = ctk.CTkFrame(
        scroll_tabla,
        fg_color="white",
        border_width=1,
        border_color="#E5E7EB",
        corner_radius=8
    )

    fila.pack(fill="x", pady=2)

    ctk.CTkLabel(
        fila,
        text=alumno[0],
        width=120
    ).grid(row=0, column=0, padx=5, pady=10)

    ctk.CTkLabel(
        fila,
        text=alumno[1],
        width=350,
        anchor="w"
    ).grid(row=0, column=1, padx=5)

    ctk.CTkLabel(
        fila,
        text=alumno[2],
        width=150
    ).grid(row=0, column=2, padx=5)

    grupo = ctk.CTkLabel(
        fila,
        text=alumno[3],
        width=70,
        fg_color="#E5E7EB",
        corner_radius=15
    )
    grupo.grid(row=0, column=3, padx=5)

    acciones = ctk.CTkFrame(
        fila,
        fg_color="transparent"
    )
    acciones.grid(row=0, column=4, padx=10)

    btn_editar = ctk.CTkButton(
        acciones,
        text="✎ Editar",
        width=90,
        height=32,
        fg_color="white",
        hover_color="#EAF3FF",
        border_width=1,
        border_color="#60A5FA",
        text_color="#2563EB"
    )
    btn_editar.pack(side="left", padx=5)

    btn_eliminar = ctk.CTkButton(
        acciones,
        text="🗑 Eliminar",
        width=90,
        height=32,
        fg_color="white",
        hover_color="#FFF1F2",
        border_width=1,
        border_color="#FCA5A5",
        text_color="#DC2626"
    )
    btn_eliminar.pack(side="left", padx=5)
app.mainloop()