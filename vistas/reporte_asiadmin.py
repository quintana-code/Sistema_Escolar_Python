from Controladores.reporte_admin_controlador import Controlador_Reporte_Admin

import customtkinter as ctk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkcalendar import DateEntry

def abrir_reporte_admin(id_usuario, nombre_usuario, rol, menu_admin):
    
  
    # ==========================
    # CONFIGURACIÓN
    # ==========================
    def exportar_reporte(): #funcion para exportar la tablita IAXD

        archivo = filedialog.asksaveasfilename(
            title="Guardar reporte",
            defaultextension=".csv",
            filetypes=[("Archivos CSV", "*.csv")]
        )

        if not archivo:
            return

        try:

            with open(
                archivo,
                "w",
                encoding="utf-8",
                newline=""
            ) as f:

                f.write(
                    "Matricula,Alumno,Fecha,Estado,Materia,Maestro\n"
                )

                for item in tabla.get_children():

                    datos = tabla.item(item)["values"]

                    f.write(
                        ",".join(map(str, datos)) + "\n"
                    )

            messagebox.showinfo(
                "Éxito",
                "Reporte exportado correctamente."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTkToplevel()
    app.title("Sistema Escolar")
    app.geometry("1200x700")

    # ==========================
    # FUNCIÓN REGRESAR
    # ==========================


    def regresar():

        app.destroy()
        menu_admin.deiconify()
    app.protocol("WM_DELETE_WINDOW", regresar)

    # ==========================
    # ESTILOS DE TABLA
    # ==========================

    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Treeview",
        rowheight=35,
        font=("Arial", 11),
        borderwidth=1,
        relief="solid"
    )

    style.configure(
        "Treeview.Heading",
        font=("Arial", 11, "bold"),
        borderwidth=2,
        relief="raised"
    )

    # ==========================
    # ENCABEZADO
    # ==========================

    frame_header = ctk.CTkFrame(app, fg_color="transparent")
    frame_header.pack(fill="x", padx=20, pady=(20, 10))

    lado_izquierdo = ctk.CTkFrame(frame_header, fg_color="transparent")
    lado_izquierdo.pack(side="left")

    titulo = ctk.CTkLabel(
        lado_izquierdo,
        text="Reportes de asistencia",
        font=("Arial", 32, "bold")
    )
    titulo.pack(anchor="w")

    subtitulo = ctk.CTkLabel(
        lado_izquierdo,
        text="Consulta registros de asistencia por rango de fechas",
        text_color="gray",
        font=("Arial", 14)
    )
    subtitulo.pack(anchor="w")

    # ==========================
    # FILTROS
    # ==========================

    frame_filtros = ctk.CTkFrame(app, corner_radius=10)
    frame_filtros.pack(fill="x", padx=20, pady=20)

    lbl_filtro = ctk.CTkLabel(
        frame_filtros,
        text="Filtros",
        font=("Arial", 18, "bold")
    )
    lbl_filtro.pack(anchor="w", padx=20, pady=(15, 0))

    lbl_desc = ctk.CTkLabel(
        frame_filtros,
        text="Selecciona el rango de fechas para consultar y PRESIONA Buscar para que logres ver los registros hasta el momento.",
        text_color="gray"
    )
    lbl_desc.pack(anchor="w", padx=20)

    frame_campos = ctk.CTkFrame(frame_filtros, fg_color="transparent")
    frame_campos.pack(fill="x", padx=20, pady=20)

    # Bloquear escritura manual
    def bloquear_teclado(event):
        return "break"

    # Fecha inicio
    fecha_inicio = DateEntry(
        frame_campos,
        date_pattern="dd/mm/yyyy",
        width=20,
        font=("Arial", 11),
        cursor="hand2",
        state="readonly"
    )
    fecha_inicio.pack(
        side="left",
        padx=(0, 10),
        ipady=6
    )

    # Fecha fin
    fecha_fin = DateEntry(
        frame_campos,
        date_pattern="dd/mm/yyyy",
        width=20,
        font=("Arial", 11),
        cursor="hand2",
        state="readonly"
    )
    fecha_fin.pack(
        side="left",
        padx=(0, 10),
        ipady=6
    )

    # Bloquear todas las teclas
    fecha_inicio.bind("<KeyPress>", bloquear_teclado)
    fecha_fin.bind("<KeyPress>", bloquear_teclado)

    # Forzar readonly después de crear los widgets
    fecha_inicio.configure(state="readonly")
    fecha_fin.configure(state="readonly")
    def consulta():

        fecha1 = fecha_inicio.get_date()
        fecha2 = fecha_fin.get_date()

        datos = Controlador_Reporte_Admin.obtener_asistencias(fecha1, fecha2)

        # limpiar tabla
        for fila in tabla.get_children():
            tabla.delete(fila)

        # cargar datos
        for registro in datos:

            tabla.insert("","end",values=registro)
            
    btn_buscar = ctk.CTkButton(
        frame_campos,
        text="Buscar",
        width=250,
        height=35,
        command= consulta
    )
    btn_buscar.pack(side="left", padx=(10, 0))
    # ==========================
    # TABLA
    # ==========================

    frame_tabla = ctk.CTkFrame(app)
    frame_tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    encabezado = ctk.CTkFrame(frame_tabla, fg_color="transparent")
    encabezado.pack(fill="x", padx=20, pady=15)

    titulo_tabla = ctk.CTkLabel(
        encabezado,
        text="Registros de asistencia",
        font=("Arial", 20, "bold")
    )
    titulo_tabla.pack(side="left")

    btn_exportar = ctk.CTkButton(
        encabezado,
        text="Exportar",
        width=100,
        command= exportar_reporte
    )
    btn_exportar.pack(side="right")

    # ==========================
    # CONTENEDOR TABLA
    # ==========================

    contenedor_tabla = ctk.CTkFrame(frame_tabla, fg_color="transparent")
    contenedor_tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    scroll_y = ttk.Scrollbar(contenedor_tabla)
    scroll_y.pack(side="right", fill="y")

    columnas = (
    "Matricula",
    "Alumno",
    "Fecha",
    "Estado",
    "Materia",
    "Maestro"
    )

    tabla = ttk.Treeview(
        contenedor_tabla,
        columns=columnas,
        show="headings",
        yscrollcommand=scroll_y.set
    )

    scroll_y.config(command=tabla.yview)

    # Columnas más visibles
    tabla.heading("Matricula", text="Matrícula")
    tabla.heading("Alumno", text="Alumno")
    tabla.heading("Fecha", text="Fecha")
    tabla.heading("Estado", text="Estado")
    tabla.heading("Materia", text="Materia")
    tabla.heading("Maestro", text="Maestro")

    tabla.column("Matricula", width=120, anchor="center")
    tabla.column("Alumno", width=250, anchor="center")
    tabla.column("Fecha", width=120, anchor="center")
    tabla.column("Estado", width=120, anchor="center")
    tabla.column("Materia", width=180, anchor="center")
    tabla.column("Maestro", width=220, anchor="center")
 #datos de bd------------------------------------------------------------
    datos = [
    ]

    for fila in datos:
        tabla.insert("", "end", values=fila)

    tabla.pack(fill="both", expand=True)