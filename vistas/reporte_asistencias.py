import customtkinter as ctk
from tkinter import ttk
from tkcalendar import DateEntry

# ======================
# CONFIGURACIÓN
# ======================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.geometry("1000x650")
ventana.title("Sistema Escolar - Reportes")
ventana.configure(fg_color="#F3F4F6")

# ======================
# HEADER
# ======================

header = ctk.CTkFrame(ventana, fg_color="white", height=60, corner_radius=0)
header.pack(fill="x")

ctk.CTkLabel(
    header,
    text="Sistema Escolar",
    font=("Arial", 18, "bold"),
    text_color="#163B65"
).place(x=20, y=15)

ctk.CTkLabel(
    header,
    text="maestro@escuela.com   |   PROFESOR",
    font=("Arial", 12),
    text_color="gray"
).place(x=750, y=18)

# ======================
# TITULO
# ======================

ctk.CTkLabel(
    ventana,
    text="Reportes de asistencia",
    font=("Arial", 28, "bold"),
    text_color="#111827"
).place(x=40, y=80)

ctk.CTkLabel(
    ventana,
    text="Consulta registros de asistencia por rango de fechas",
    font=("Arial", 14),
    text_color="gray"
).place(x=40, y=120)

# ======================
# FILTROS
# ======================

card_filtros = ctk.CTkFrame(
    ventana,
    width=920,
    height=140,
    fg_color="white",
    corner_radius=15
)
card_filtros.place(x=40, y=160)

ctk.CTkLabel(
    card_filtros,
    text="Filtros",
    font=("Arial", 14, "bold")
).place(x=20, y=15)

ctk.CTkLabel(
    card_filtros,
    text="Selecciona el rango de fechas para consultar",
    text_color="gray"
).place(x=20, y=40)

# ======================
# CALENDARIOS (CORREGIDOS)
# ======================

fecha_inicio = DateEntry(
    card_filtros,
    width=18,
    date_pattern="yyyy-mm-dd",
    year=2025,
    mindate=None,
    maxdate=None,
    selectmode="day"
)
fecha_inicio.place(x=20, y=80)

fecha_fin = DateEntry(
    card_filtros,
    width=18,
    date_pattern="yyyy-mm-dd",
    year=2025,
    mindate=None,
    maxdate=None,
    selectmode="day"
)
fecha_fin.place(x=250, y=80)

# ======================
# BOTÓN BUSCAR
# ======================

ctk.CTkButton(
    card_filtros,
    text="🔍 Buscar",
    width=200,
    fg_color="#163B65",
    hover_color="#0f2d4d"
).place(x=480, y=80)

# ======================
# TABLA
# ======================

card_tabla = ctk.CTkFrame(
    ventana,
    width=920,
    height=350,
    fg_color="white",
    corner_radius=15
)
card_tabla.place(x=40, y=320)

ctk.CTkLabel(
    card_tabla,
    text="Registros de asistencia",
    font=("Arial", 14, "bold")
).place(x=20, y=15)

ctk.CTkLabel(
    card_tabla,
    text="Total: 0 registros",
    text_color="gray"
).place(x=20, y=40)

# ======================
# FRAME TABLA + SCROLL
# ======================

tabla_frame = ctk.CTkFrame(
    card_tabla,
    width=880,
    height=240,
    fg_color="white"
)
tabla_frame.place(x=20, y=80)

scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical")

tabla = ttk.Treeview(
    tabla_frame,
    columns=("est", "fecha", "estado", "marcado"),
    show="headings",
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=tabla.yview)
scrollbar.pack(side="right", fill="y")

tabla.pack(side="left", fill="both", expand=True)

# COLUMNAS
tabla.heading("est", text="Estudiante")
tabla.heading("fecha", text="Fecha")
tabla.heading("estado", text="Estado")
tabla.heading("marcado", text="Marcado por")

tabla.column("est", width=200)
tabla.column("fecha", width=120)
tabla.column("estado", width=120)
tabla.column("marcado", width=150)

# EJEMPLO
tabla.insert("", "end", values=(
    "No hay registros para el rango seleccionado",
    "",
    "",
    ""
))

ventana.mainloop()