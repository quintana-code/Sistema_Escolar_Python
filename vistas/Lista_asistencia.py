import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from datetime import datetime
import csv

# ---------------- CONFIGURACIÓN ----------------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Toma de Asistencia")
ventana.geometry("1000x700")

# ---------------- ICONOS ----------------

icono_presente = ctk.CTkImage(
    Image.open("iconos/presente.png"),
    size=(20, 20)
)

icono_falta = ctk.CTkImage(
    Image.open("iconos/falta.png"),
    size=(20, 20)
)

icono_retardo = ctk.CTkImage(
    Image.open("iconos/retardo.png"),
    size=(20, 20)
)

# ---------------- ALUMNOS ----------------

alumnos = [
    "Ana Martínez",
    "Carlos Rodríguez",
    "Diego Morales",
    "Elena Castillo",
    "Juan García",
    "Laura Fernández",
    "María López",
    "Pedro Sánchez",
    "Sofía Hernández",
    "Miguel Torres",
    "Luis Ramírez",
    "Andrea Pérez",
    "Valeria Cruz",
    "Fernando Díaz",
    "Ricardo Gómez",
    "Patricia Flores",
    "Roberto Castillo",
    "José López",
    "Daniela Ruiz",
    "Alejandro Morales"
]

# ---------------- VARIABLES ----------------

asistencias = {}

fecha_actual = datetime.now().strftime("%d/%m/%Y")

# ---------------- FUNCIONES ----------------

def registrar_asistencia(nombre, estado, etiqueta):
    asistencias[nombre] = estado
    etiqueta.configure(text=estado)

def guardar_asistencia():

    try:

        with open(
            "asistencia.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow(["Fecha", fecha_actual])
            escritor.writerow(["Total alumnos", len(alumnos)])
            escritor.writerow([])

            escritor.writerow([
                "Alumno",
                "Estado"
            ])

            for alumno in alumnos:

                estado = asistencias.get(
                    alumno,
                    "Sin registrar"
                )

                escritor.writerow([
                    alumno,
                    estado
                ])

        messagebox.showinfo(
            "Éxito",
            "Asistencia guardada correctamente."
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

# ---------------- ENCABEZADO ----------------

frame_info = ctk.CTkFrame(
    ventana,
    corner_radius=15
)

frame_info.pack(
    fill="x",
    padx=20,
    pady=15
)

titulo = ctk.CTkLabel(
    frame_info,
    text="📋 Toma de Asistencia",
    font=("Arial", 28, "bold")
)

titulo.pack(
    anchor="w",
    padx=20,
    pady=(15, 5)
)

lbl_fecha = ctk.CTkLabel(
    frame_info,
    text=f"Fecha: {fecha_actual}",
    font=("Arial", 15)
)

lbl_fecha.pack(
    anchor="w",
    padx=20
)

lbl_total = ctk.CTkLabel(
    frame_info,
    text=f"Total de alumnos: {len(alumnos)}",
    font=("Arial", 15, "bold")
)

lbl_total.pack(
    anchor="w",
    padx=20,
    pady=(0, 15)
)

# ---------------- SCROLL ----------------

frame_scroll = ctk.CTkScrollableFrame(
    ventana,
    width=940,
    height=450
)

frame_scroll.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

# ---------------- FILAS ----------------

for alumno in alumnos:

    fila = ctk.CTkFrame(
        frame_scroll,
        corner_radius=12
    )

    fila.pack(
        fill="x",
        padx=10,
        pady=5
    )

    lbl_nombre = ctk.CTkLabel(
        fila,
        text=alumno,
        font=("Arial", 15, "bold"),
        width=250,
        anchor="w"
    )

    lbl_nombre.pack(
        side="left",
        padx=15,
        pady=10
    )

    lbl_estado = ctk.CTkLabel(
        fila,
        text="Sin registrar",
        width=120
    )

    lbl_estado.pack(
        side="left",
        padx=10
    )

    # PRESENTE

    btn_presente = ctk.CTkButton(
        fila,
        text=" Presente",
        image=icono_presente,
        compound="left",
        width=120,
        fg_color="#28A745",
        hover_color="#218838",
        command=lambda a=alumno, l=lbl_estado:
        registrar_asistencia(
            a,
            "Presente",
            l
        )
    )

    btn_presente.pack(
        side="right",
        padx=5
    )

    # RETARDO

    btn_retardo = ctk.CTkButton(
        fila,
        text=" Retardo",
        image=icono_retardo,
        compound="left",
        width=120,
        fg_color="#FF9800",
        hover_color="#E68900",
        command=lambda a=alumno, l=lbl_estado:
        registrar_asistencia(
            a,
            "Retardo",
            l
        )
    )

    btn_retardo.pack(
        side="right",
        padx=5
    )

    # AUSENTE

    btn_ausente = ctk.CTkButton(
        fila,
        text=" Ausente",
        image=icono_falta,
        compound="left",
        width=120,
        fg_color="#DC3545",
        hover_color="#C82333",
        command=lambda a=alumno, l=lbl_estado:
        registrar_asistencia(
            a,
            "Ausente",
            l
        )
    )

    btn_ausente.pack(
        side="right",
        padx=5
    )

# ---------------- BOTÓN GUARDAR ----------------

btn_guardar = ctk.CTkButton(
    ventana,
    text="Guardar Asistencia",
    fg_color="red",
    hover_color="#B30000",
    width=300,
    height=45,
    font=("Arial", 16, "bold"),
    command=guardar_asistencia
)

btn_guardar.pack(
    pady=20
)

# ---------------- EJECUTAR ----------------

ventana.mainloop()