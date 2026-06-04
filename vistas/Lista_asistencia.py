from Controladores.alumno_controlador import Controlador_Alumno
from Controladores.materia_controlador import Controlador_Materia
from Modulos.asistencia import Asistencia

from tkinter import messagebox # para ventanas emergentes
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from datetime import datetime


def abrir_listaAsistencia(menu_maestro, id_usuario):
    # ---------------- CONFIGURACIÓN ----------------

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    ventana = ctk.CTkToplevel() #abrirlacomo una ventana secundaria en vez de una principal
    ventana.title("Toma de Asistencia")
    ventana.geometry("1000x700")
    def regresar_menu():

        ventana.destroy()
        menu_maestro.deiconify()
            
        #al presionar 'x" lo regresará al inicio menu de maestro
    ventana.protocol(
        "WM_DELETE_WINDOW",
        regresar_menu #sin parentesis
        )
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

    # ---------------- ALUMNOS en la BASE DE DATOS----------------

    alumnosen_bd = Controlador_Alumno.obtener_alumnos()
    #construir filas de manera automatica

    # ---------------- VARIABLES ----------------

    asistencias = {}

    fechaen_bd = datetime.now().strftime("%Y-%m-%d")

    # ---------------- FUNCIONES ----------------
    
    def registrar_asistencia(id_alumno, estado, etiqueta):

        asistencias[id_alumno] = estado
        etiqueta.configure(text=estado)

    def guardar_asistencia():

        confirmar = messagebox.askyesno("Confirmar","¿Deseas guardar la asistencia?")
        if not confirmar:
            return
        try:
            print("ID USUARIO RECIBIDO:", id_usuario)
            materia = Controlador_Materia.obtener_materia_por_usuario(
                id_usuario
            )

            if not materia:
                messagebox.showerror(
                    "Error",
                    "No hay materia asignada al maestro."
                )
                return

            id_materia = materia[0]

            for alumno in alumnosen_bd:

                id_alumno = alumno[0]

                estado = asistencias.get(
                    id_alumno,
                    "Ausente"
                )

                asistencia = Asistencia(
                    None,
                    fechaen_bd,
                    estado,
                    id_alumno,
                    id_materia
                )

                asistencia.guardar_Asistencia()

            messagebox.showinfo(
                "Éxito", "Asistencia guardada correctamente.")
            ventana.destroy()          # Cierra la lista de asistencia
            menu_maestro.deiconify()   # Vuelve a mostrar el menú maestro)

        except Exception as e:
            messagebox.showerror("Error",str(e))
    
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
        text=f"Fecha: {fechaen_bd}",
        font=("Arial", 15)
    )

    lbl_fecha.pack(
        anchor="w",
        padx=20
    )

    lbl_total = ctk.CTkLabel(
        frame_info,
        text=f"Total de alumnos: {len(alumnosen_bd)}",
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

    for alumno in alumnosen_bd:
        id_alumno = alumno[0]
        nombre = alumno[1]
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
            text=nombre,
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
            command=lambda i=id_alumno, l=lbl_estado:
            registrar_asistencia(
                i,
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
            command=lambda i=id_alumno, l=lbl_estado:
            registrar_asistencia(
                i,
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
            command=lambda i=id_alumno, l=lbl_estado:
            registrar_asistencia(
                i,
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

