from conexion.conexion import Conexion

import tkinter as tk
from tkinter import messagebox # para ventanas emergentes
from PIL import Image, ImageTk


def abrir_menu_maestro(id_usuario,nombre_usuario, rol):
    # ------------------------
    # Funciones
    # ------------------------

    def tomar_asistencia():
        ventana.withdraw() #ocultar ventana para abrir la otra
        from vistas.Lista_asistencia import abrir_listaAsistencia
        abrir_listaAsistencia(ventana, id_usuario)


    def consultar_asistencia():
        ventana.withdraw()
        from vistas.reporte_asistencias import abrir_reporte_asistencias
        abrir_reporte_asistencias(ventana,id_usuario,nombre_usuario, rol)

    def cerrar_sesion():

        respuesta = messagebox.askyesno(
            "Cerrar sesión","¿Deseas cerrar sesión y volver al inicio?",icon="warning"
        )

        if respuesta:
            ventana.destroy()
            #para evitar que menu cargue antes que main, lo pondremos aqui :3
            from vistas.loginprincipal import abrir_login_principal
            abrir_login_principal()


    # ------------------------
    # Ventana
    # ------------------------

    ventana = tk.Tk()
    ventana.title("Sistema Escolar")
    ventana.geometry("900x650")
    ventana.configure(bg="#e8e8e8")
    ventana.resizable(False, False)


    # ------------------------
    # Cargar iconos
    # ------------------------

    icono_asistencia = ImageTk.PhotoImage(
        Image.open("iconos/asistencia.png").resize((40, 40))
    )

    icono_consulta = ImageTk.PhotoImage(
        Image.open("iconos/consulta.png").resize((40, 40))
    )

    icono_salir = ImageTk.PhotoImage(
        Image.open("iconos/salir.png").resize((40, 40))
    )


    # ------------------------
    # Contenedor principal
    # ------------------------

    contenedor = tk.Frame(
        ventana,
        bg="white",
        width=750,
        height=550
    )

    contenedor.place(relx=0.5, rely=0.5, anchor="center")


    # ------------------------
    # Encabezado
    # ------------------------

    titulo = tk.Label(
        contenedor,
        text="Menú principal",
        font=("Arial", 24, "bold"),
        bg="white",
        fg="#173f73"
    )

    titulo.place(x=40, y=25)

    profesor = tk.Label(
        contenedor,
        text="PROFESOR",
        font=("Arial", 10),
        bg="white",
        fg="gray"
    )

    profesor.place(x=42, y=65)


    # ------------------------
    # Bienvenida
    # ------------------------

    bienvenida = tk.Frame(
        contenedor,
        bg="#f7f7f7",
        width=620,
        height=120,
        highlightbackground="#d9d9d9",
        highlightthickness=1
    )

    bienvenida.place(x=60, y=100)

    tk.Label(
        bienvenida,
        text="BIENVENIDO AL SISTEMA",
        font=("Arial", 10, "bold"),
        bg="#f7f7f7",
        fg="#173f73"
    ).place(x=20, y=20)

    tk.Label(
        bienvenida,
        text="Prof. Maestro",
        font=("Arial", 18, "bold"),
        bg="#f7f7f7"
    ).place(x=20, y=45)

    tk.Label(
        bienvenida,
        text="Seleccione una opción para gestionar la asistencia.",
        font=("Arial", 10),
        bg="#f7f7f7",
        fg="gray"
    ).place(x=20, y=80)


    # ------------------------
    # Tarjetas
    # ------------------------

    def crear_tarjeta(x, y, titulo, descripcion, icono, comando):

        tarjeta = tk.Frame(
            contenedor,
            bg="white",
            width=280,
            height=110,
            highlightbackground="#d9d9d9",
            highlightthickness=1,
            cursor="hand2"
        )

        tarjeta.place(x=x, y=y)

        lbl_icono = tk.Label(
            tarjeta,
            image=icono,
            bg="white"
        )
        lbl_icono.place(x=15, y=30)

        lbl_titulo = tk.Label(
            tarjeta,
            text=titulo,
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#173f73"
        )
        lbl_titulo.place(x=70, y=25)

        lbl_desc = tk.Label(
            tarjeta,
            text=descripcion,
            font=("Arial", 9),
            bg="white",
            fg="gray"
        )
        lbl_desc.place(x=70, y=55)

        # Click en toda la tarjeta
        tarjeta.bind("<Button-1>", lambda e: comando())
        lbl_icono.bind("<Button-1>", lambda e: comando())
        lbl_titulo.bind("<Button-1>", lambda e: comando())
        lbl_desc.bind("<Button-1>", lambda e: comando())


    # ------------------------
    # Crear tarjetas
    # ------------------------

    crear_tarjeta(
        60, 260,
        "Tomar asistencia",
        "Registrar asistencia diaria",
        icono_asistencia,
        tomar_asistencia
    )

    crear_tarjeta(
        370, 260,
        "Consultar asistencias",
        "Ver historial de alumnos",
        icono_consulta,
        consultar_asistencia
    )

    # ------------------------
    # Cerrar sesión centrado
    # ------------------------

    crear_tarjeta(
        235, 390,  # centrado en 750px de ancho
        "Cerrar sesión",
        "Salir del sistema",
        icono_salir,
        cerrar_sesion
    )
    


    ventana.mainloop()
