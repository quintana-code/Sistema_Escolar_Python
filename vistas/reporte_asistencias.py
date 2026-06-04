
from Controladores.reporte_controlador import Controlador_Reporte

import customtkinter as ctk
from tkinter import ttk, filedialog, messagebox
from tkcalendar import DateEntry

def abrir_reporte_asistencias(menu_maestro, id_usuario, nombre_usuario, rol_usuario):
    
    def exportar_reporte():

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

                f.write("Estudiante,Fecha,Estado,Materia\n")

                for item in tabla.get_children():

                    datos = tabla.item(item)["values"]

                    f.write(
                        ",".join(map(str, datos))+ "\n")

            messagebox.showinfo(
                "Éxito",
                "Reporte exportado correctamente."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )
    

    def buscar_asistencias():

        #para Limpiar tabla (ia)
        for item in tabla.get_children():
            tabla.delete(item)

        fecha_ini = fecha_inicio.get()
        fecha_fin_texto = fecha_fin.get()

        #verificar que la fecha tenga coherencia :3
        if fecha_ini > fecha_fin_texto:

            messagebox.showwarning(
                "Fechas inválidas", "La fecha inicial no puede ser mayor a la fecha final."
            )

            return
        try:
            registros = Controlador_Reporte.obtener_asistencias(fecha_ini, fecha_fin_texto,id_usuario)

            for fila in registros:

                tabla.insert(
                    "",
                    "end",
                    values=fila
                )

            lbl_total.configure(
                text=f"Total: {len(registros)} registros"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ======================
    # CONFIGURACIÓN
    # ======================

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    ventana = ctk.CTkToplevel()
    ventana.geometry("1000x750")
    ventana.title("Sistema Escolar - Reportes")
    ventana.configure(fg_color="#F3F4F6")
    ventana.grab_set()
    ventana.focus()

    def regresar_menu():

        ventana.destroy()
        menu_maestro.deiconify()
        
    #al presionar 'x" lo regresará al inicio menu de maestro
    ventana.protocol(
        "WM_DELETE_WINDOW",
        regresar_menu
    )

    # ======================
    # HEADER
    # ======================

    header = ctk.CTkFrame(
        ventana,
        fg_color="white",
        height=60,
        corner_radius=0
    )
    header.pack(fill="x")

    ctk.CTkLabel(
        header,
        text="Sistema Escolar",
        font=("Arial", 18, "bold"),
        text_color="#163B65"
    ).place(x=20, y=15)
    #para que aparesca quien tiene la sesion iniciada :o y su rol
    ctk.CTkLabel(
    header,
    text=f"{nombre_usuario}   |   {rol_usuario}",
    font=("Arial", 12),
    text_color="gray"
    ).place(x=720, y=18)

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
    # FECHAS
    # ======================
    fecha_inicio = DateEntry(
        card_filtros,
        width=18,
        date_pattern="yyyy-mm-dd",
        state="normal"
    )
    fecha_inicio.place(x=20, y=80)

    fecha_fin = DateEntry(
        card_filtros,
        width=18,
        date_pattern="yyyy-mm-dd",
        state="normal"
    )
    fecha_fin.place(x=250, y=80)

    # ======================
    # BOTÓN BUSCAR
    # ======================
    ctk.CTkButton(
    card_filtros,
    text="🔍 Buscar",
    width=200, fg_color="#163B65",
    hover_color="#0f2d4d",
    command=buscar_asistencias
    ).place(x=480, y=80)

    # ======================
    # CARD TABLA
    # ======================

    card_tabla = ctk.CTkFrame(
        ventana,
        width=920,
        height=420,
        fg_color="white",
        corner_radius=15
    )
    card_tabla.place(x=40, y=320)

    ctk.CTkLabel(
        card_tabla,
        text="Registros de asistencia",
        font=("Arial", 14, "bold")
    ).place(x=20, y=15)

    lbl_total = ctk.CTkLabel(
    card_tabla,
    text="Total: 0 registros",
    text_color="gray"
    )

    lbl_total.place(
        x=20,
        y=40
    )
    # ======================
    # BOTÓN EXPORTAR
    # ======================

    ctk.CTkButton(
        card_tabla,
        text="📄 Exportar CSV",
        width=150,
        height=35,
        fg_color="#163B65",
        hover_color="#0f2d4d",
        command=exportar_reporte
    ).place(x=730, y=20)

    # ======================
    # FRAME TABLA
    # ======================

    tabla_frame = ctk.CTkFrame(
        card_tabla,
        width=880,
        height=320,
        fg_color="white"
    )

    tabla_frame.place(
        x=20,
        y=80
    )

    # ======================
    # SCROLLS
    # ======================

    scroll_y = ttk.Scrollbar(
        tabla_frame,
        orient="vertical"
    )

    scroll_x = ttk.Scrollbar(
        tabla_frame,
        orient="horizontal"
    )

    # ======================
    # TABLA
    # ======================

    tabla = ttk.Treeview(
        tabla_frame,
        columns=("est", "fecha", "estado", "materia"),
        show="headings",
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )

    scroll_y.config(command=tabla.yview)
    scroll_x.config(command=tabla.xview)

    # ======================
    # ENCABEZADOS
    # ======================

    tabla.heading("est", text="Estudiante")
    tabla.heading("fecha", text="Fecha")
    tabla.heading("estado", text="Estado")
    tabla.heading("materia", text="Materia")

    # ======================
    # COLUMNAS
    # ======================

    tabla.column(
        "est",
        width=450,
        minwidth=400,
        anchor="w"
    )

    tabla.column(
        "fecha",
        width=150,
        anchor="center"
    )

    tabla.column(
        "estado",
        width=150,
        anchor="center"
    )

    tabla.column(
        "materia",
        width=200,
        anchor="center"
    )

    # ======================
    # EMPAQUETAR
    # ======================

    scroll_y.pack(side="right", fill="y")
    scroll_x.pack(side="bottom", fill="x")

    tabla.pack(
        side="left",
        fill="both",
        expand=True
    )

    

  