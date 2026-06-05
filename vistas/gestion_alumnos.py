import customtkinter as ctk
from Controladores.alumno_controlador import Controlador_Alumno

from tkinter import messagebox
def abrir_gestiona_alumnos(id_usuario, nombre_usuario, rol, menu_admin):

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTkToplevel()
    app.geometry("1200x700")
    app.title("Gestión de alumnos")

    # ==========================
    # ENCABEZADO
    # ==========================
    def regresar_menu():
        app.destroy()
        menu_admin.deiconify()
            
    #al presionar 'x" lo regresará al inicio menu de maestro
    app.protocol("WM_DELETE_WINDOW",regresar_menu
        )
    def agregar_alumno():

        ventana = ctk.CTkToplevel(app)
        ventana.title("Agregar alumno")
        ventana.geometry("400x400")

        ventana.transient(app)
        ventana.grab_set()
        ventana.focus_force()
        ventana.lift()

        ctk.CTkLabel(ventana, text="ID Alumno"
        ).pack(pady=(20,5))

        entry_id = ctk.CTkEntry(ventana,width=250)
        entry_id.pack()
        ctk.CTkLabel(ventana, text="Nombre").pack(pady=(20,5))

        entry_nombre = ctk.CTkEntry(ventana, width=250)
        entry_nombre.pack()

        ctk.CTkLabel(ventana,text="Grupo").pack(pady=(15,5))

        entry_grupo = ctk.CTkEntry(
            ventana,
            width=250
        )
        entry_grupo.pack()
    #guardar en el formulario mini---------------------------------------------------------------
        def guardar():
            id_alumno = entry_id.get().strip()
            nombre = entry_nombre.get().strip()
            grupo = entry_grupo.get().strip()
    #validacion por si los campos estan vaciós-----------------------------------------------------
            if id_alumno == "" or nombre == "" or grupo == "":
                messagebox.showwarning("Campos vacíos","Completa todos los campos")
                return

            agregado = Controlador_Alumno.agregar_alumno(id_alumno,nombre,grupo)

            if agregado:

                messagebox.showinfo("Éxito","Alumno agregado correctamente")

                ventana.destroy()

                app.destroy()

                abrir_gestiona_alumnos(id_usuario, nombre_usuario,rol, menu_admin)

            else:

                messagebox.showerror("Error","No se pudo agregar el alumno")

        ctk.CTkButton(
            ventana,
            text="Guardar",
            command=guardar
        ).pack(pady=20)

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
        font=("Arial", 14, "bold"),
        command= agregar_alumno
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
    # ENCABEZADOS de tabla
    # ==========================

    encabezado = ctk.CTkFrame(
        scroll_tabla,
        fg_color="#F8FAFC",
        corner_radius=10
    )
#--------------------------------------ENCABEZADOS DE LA TABLA........................................................
    encabezado.pack(fill="x", pady=(0, 5))

    # MISMA DISTRIBUCIÓN QUE LAS FILAS  DE LA TABLA
    encabezado.grid_columnconfigure(0, weight=1, uniform="columnas")
    encabezado.grid_columnconfigure(1, weight=4, uniform="columnas")
    encabezado.grid_columnconfigure(2, weight=1, uniform="columnas")
    encabezado.grid_columnconfigure(3, weight=2, uniform="columnas")

#LABELS DEL HEADER
    ctk.CTkLabel(
        encabezado,
        text="ID",
        font=("Arial", 12, "bold")
    ).grid(row=0, column=0, padx=10, pady=10, sticky="ew") #PARA que se expandan dentro de su celda

    ctk.CTkLabel(
        encabezado,
        text="NOMBRE",
        font=("Arial", 12, "bold")
    ).grid(row=0, column=1, padx=10,sticky="ew")

    ctk.CTkLabel(
        encabezado,
        text="GRUPO",
        font=("Arial", 12, "bold")
    ).grid(row=0, column=2, padx=10, sticky="ew")

    ctk.CTkLabel(
        encabezado,
        text="ACCIONES",
        font=("Arial", 12, "bold")
    ).grid(row=0, column=3, padx=10, sticky="ew")

    # ==========================
    # DATOS DE LA BD
    # ==========================
    datos = Controlador_Alumno.obtener_alumnos_admin()

    contador.configure(text=f"{len(datos)} registros")

    def eliminar_alumno(id_alumno):

        confirmar = messagebox.askyesno(
            "Eliminar alumno",  
            "¿Seguro de que deseas eliminar este alumno?"
        )

        if confirmar:

            eliminado = Controlador_Alumno.eliminar_alumno( id_alumno)

            if eliminado:

                messagebox.showinfo("Éxito","Alumno eliminado correctamente!"
                )

                app.destroy()

                abrir_gestiona_alumnos(id_usuario, nombre_usuario, rol, menu_admin)

            else:
                messagebox.showerror("Error", "No se pudo eliminar el alumno")

    def editar_alumno(id_alumno, nombre_actual, grupo_actual):
        #creacion del mini formulario para editar
        ventana = ctk.CTkToplevel(app)
        ventana.title("Editar alumno")
        ventana.geometry("400x250")
        #FUNCIONES PARA QUE LA MINI PANTALLA NO SE VAYAS ATRAS DE LA INTERFAZ IA
        ventana.transient(app)   # la vincula a la ventana principal
        ventana.grab_set()       # bloquea interacción con la ventana padre
        ventana.focus_force()    # le da el foco inmediatamente
        ventana.lift()           # la trae al frente
#---------------------------------------------------------------------------------------------------------------
        ctk.CTkLabel(
            ventana,
            text="Nombre"
        ).pack(pady=(20,5))

        entry_nombre = ctk.CTkEntry(
            ventana,
            width=250
        )
        entry_nombre.pack()
        entry_nombre.insert(0, nombre_actual)

        ctk.CTkLabel(
            ventana,
            text="Grupo"
        ).pack(pady=(15,5))

        entry_grupo = ctk.CTkEntry(
            ventana,
            width=250
        )
        entry_grupo.pack()
        entry_grupo.insert(0, grupo_actual)

        def guardar():

            nombre = entry_nombre.get().strip()
            grupo = entry_grupo.get().strip()

            if nombre == "" or grupo == "":
                messagebox.showwarning("Campos vacíos","Completa todos los campos"
                )
                return

            actualizado = Controlador_Alumno.editar_alumno(id_alumno, nombre, grupo
            )

            if actualizado:

                messagebox.showinfo(
                    "Éxito","Alumno actualizado correctamente"
                )

                ventana.destroy()

                app.destroy()
                abrir_gestiona_alumnos(
                    id_usuario, nombre_usuario,rol, menu_admin
                )

            else:

                messagebox.showerror(
                    "Error",
                    "No se pudo actualizar el alumno"
                )
    #boton giardar en el formulario de editar
        ctk.CTkButton(
            ventana,
            text="Guardar cambios",
            command=guardar
        ).pack(pady=20)

    for alumno in datos:

        fila = ctk.CTkFrame(
            scroll_tabla,
            fg_color="white",
            border_width=1,
            border_color="#E5E7EB",
            corner_radius=8
        )
        fila.pack(fill="x", pady=4, padx =5)

        # CONFIGURACIÓN COLUMNAS FILA
        fila.grid_columnconfigure(0, weight=1, uniform="columnas")
        fila.grid_columnconfigure(1, weight=4, uniform="columnas")
        fila.grid_columnconfigure(2, weight=1, uniform="columnas")
        fila.grid_columnconfigure(3, weight=2, uniform="columnas")

        #ID
        ctk.CTkLabel(
            fila,
            text=alumno[0]
        ).grid(row=0, column=0, padx=10, pady=12, sticky="ew")

        #NOMBRE
        ctk.CTkLabel(
            fila,
            text=alumno[1],
            anchor="w"
        ).grid(row=0, column=1, padx=10, sticky="w")

        #GRUPO
        grupo = ctk.CTkLabel(
            fila,
            text=alumno[2],
            width=70,
            fg_color="#E5E7EB",
            corner_radius=15
        )
        grupo.grid(row=0, column=2)

        #ACCIONES
        acciones = ctk.CTkFrame(
            fila,
            fg_color="transparent"
        )
        acciones.grid(row=0, column=3, pady=10)

        btn_editar = ctk.CTkButton(
            acciones,
            text="✎ Editar",
            width=90,
            height=32,
            fg_color="white",
            hover_color="#EAF3FF",
            border_width=1,
            border_color="#60A5FA",
            text_color="#2563EB",
            command=lambda a=alumno: editar_alumno(a[0], a[1], a[2]) #id, nombre, grupo
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
            text_color="#DC2626",
            command=lambda id_alumno = alumno[0]: eliminar_alumno(id_alumno)
        )
        btn_eliminar.pack(side="left", padx=5)