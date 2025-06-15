from tkinter import *
from tkinter import ttk
import ast
from tkcalendar import DateEntry
from datetime import datetime
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Usuarios import consultas

def menu():
    reporteGui = Tk()
    reporteGui.title("Reporte Financiero")
    reporteGui.geometry("300x150")
    frame = ttk.Frame(reporteGui, padding=20)
    frame.pack(expand=True)
    lbFechaInicio = ttk.Label(frame, text="Fecha Inicio: ")
    lbFechaInicio.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    date_inicio = DateEntry(frame, width=12,  date_pattern='yyyy-mm-dd')
    date_inicio.grid(row=0, column=1, padx=5, pady=5)
    lbFechaFin = ttk.Label(frame, text="Fecha Fin: ", foreground="black", background="white")
    lbFechaFin.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    date_fin = DateEntry(frame, width=12,  date_pattern='yyyy-mm-dd')
    date_fin.grid(row=1, column=1, padx=5, pady=5)
    btn_informe = ttk.Button(frame, text="Reporte", command=lambda: informe(reporteGui, date_inicio.get(), date_fin.get()))
    btn_informe.grid(row=2, column=0, padx=5, pady=5)
    
    reporteGui.mainloop()
    
def informe(reporteGui, fechaInicio, fechaFin):
    
    print(fechaInicio)
    resultados = consultas(f"""
            select fecha_factura as Fecha, CONCAT(Cli.nombre, ' ', Cli.apellido) as Cliente, Pl.descripcion as Servicio,  
			Monto, TP.descripcion as 'Tipo de Pago' 
			from facturacion as F
            inner join contratos as C On C.id_contrato = F.id_contrato
			inner join clientes as Cli on cli.id_clientes = C.id_cliente
			inner join planes as Pl on Pl.id_planes = C.id_plan
			inner join tipo_pagos as TP on TP.id_tipo_pago = C.id_tipo_pago
            where fecha_factura    between '{fechaInicio}' and '{fechaFin}'
        """)
    ventana = Toplevel(reporteGui)
    columnas = ("Fecha", "Cliente", "Servicio", "Monto", "Tipo de Pago")
    tree = ttk.Treeview(ventana, columns=columnas, show="headings")
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    usuarios_limpios = []

    for fila in resultados:
        # Paso 1: convertir a tupla real si viene como string
        if isinstance(fila, str):
            fila = ast.literal_eval(fila)

        # Paso 2: limpiar comillas simples (solo si se necesita)
        fila_limpia = tuple(
            str(dato).strip().strip("'") if dato is not None else "" for dato in fila
        )

        usuarios_limpios.append(fila_limpia)

    for fila in usuarios_limpios:
        tree.insert("", "end", values=fila)

    tree.pack(expand=True, fill="both")    
    
    
menu()    