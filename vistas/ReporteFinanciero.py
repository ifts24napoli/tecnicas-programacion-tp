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
    btn_facturacion = ttk.Button(frame, text="Facturaion", command=lambda: facturacion(reporteGui, date_inicio.get(), date_fin.get()))
    btn_facturacion.grid(row=2, column=0, padx=5, pady=5)
    btn_rendimiento = ttk.Button(frame, text="Rendimientos", command=lambda: rendimientos(date_inicio.get(), date_fin.get()))
    btn_rendimiento.grid(row=2, column=1, padx=5, pady=5)
    
    reporteGui.mainloop()
    
def facturacion(reporteGui, fechaInicio, fechaFin):
    resultados = consultas(f"""
            select C.id_Contrato, fecha_factura as Fecha, CONCAT(Cli.nombre, ' ', Cli.apellido) as Cliente, Pl.descripcion as Servicio,  
			Monto, TP.descripcion as 'Tipo de Pago', F.estado 
			from facturacion as F
            inner join contratos as C On C.id_contrato = F.id_contrato
			inner join clientes as Cli on cli.id_clientes = C.id_cliente
			inner join planes as Pl on Pl.id_planes = C.id_plan
			inner join tipo_pagos as TP on TP.id_tipo_pago = C.id_tipo_pago
            where fecha_factura  between '{fechaInicio}' and '{fechaFin}'
        """)
    ventana = Toplevel(reporteGui)
    columnas = ("id_Contrato", "Fecha", "Cliente", "Servicio/Plan", "Monto", "Tipo de Pago", "Estado")
    tree = ttk.Treeview(ventana, columns=columnas, show="headings")
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    reporte_limpio = []

    for fila in resultados:
        # Paso 1: convertir a tupla real si viene como string
        if isinstance(fila, str):
            fila = ast.literal_eval(fila)

        # Paso 2: limpiar comillas simples (solo si se necesita)
        fila_limpia = tuple(
            str(dato).strip().strip("'") if dato is not None else "" for dato in fila
        )

        reporte_limpio.append(fila_limpia)

    for fila in reporte_limpio:
        tree.insert("", "end", values=fila)

    tree.pack(expand=True, fill="both")    
    def doble_click(event):
        item = tree.selection()
        if item:
            valores = tree.item(item[0], 'values')
            comodatos(valores, tree , ventana)

    tree.bind("<Double-1>", doble_click)
    
    def comodatos(valores, tree, ventana):        
        resultados = consultas(f"""select I.codigo, I.descripcion,  cantidad
                                    from comodatos as Com
                                    inner join inventario as I On I.id_inventario = Com.id_inventario
                                    inner join contratos as Contr ON Contr.id_contrato = Com.id_contrato
                                    inner join clientes as Cli On cli.id_clientes = Contr.id_cliente
                                    where Contr.id_contrato = {valores[0]}  """)
        ventana = Toplevel(reporteGui)
        ventana.title(f"Comodatos: {valores[2]}")
        columnas = ("Codigo", "Descripcion", "Cantidad")
        tree = ttk.Treeview(ventana, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        reporte_limpio = []

        for fila in resultados:
            # Paso 1: convertir a tupla real si viene como string
            if isinstance(fila, str):
                fila = ast.literal_eval(fila)

            # Paso 2: limpiar comillas simples (solo si se necesita)
            fila_limpia = tuple(
                str(dato).strip().strip("'") if dato is not None else "" for dato in fila
            )

            reporte_limpio.append(fila_limpia)

        for fila in reporte_limpio:
            tree.insert("", "end", values=fila)
        tree.pack(expand=True, fill="both")   

def rendimientos(fechaInicio, fechaFin):
    resultados = consultas(f"""select sum(monto) as Total, COUNT(*) as Cantidad
                                from facturacion
                                where fecha_factura between '{fechaInicio}' and '{fechaFin}'""")
    print(resultados[0][0])
    rendimientoGui = Tk()
    rendimientoGui.title("Rendimiento")
    rendimientoGui.geometry("300x150")
    frame = ttk.Frame(rendimientoGui, padding=20)
    frame.pack(expand=True)
    lbFechaInicio = ttk.Label(frame, text="Fecha Inicio: ")
    lbFechaInicio.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    lbfechaInicioIngresada = ttk.Label(frame, text=f"{fechaInicio}")
    lbfechaInicioIngresada.grid(row=0, column=1, sticky="w", padx=5, pady=5)
    lbFechaFin = ttk.Label(frame, text="Fecha Fin: ")
    lbFechaFin.grid(row=1, column=0, sticky="w", padx=5, pady=5 )
    lbFechaFinIngresada = ttk.Label(frame, text=f"{fechaFin}")
    lbFechaFinIngresada.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    lbFacturacionTotal = ttk.Label(frame, text="Facturacion Total: ")
    lbFacturacionTotal.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    if resultados[0][0] != None:
        lbTotal = ttk.Label(frame, text=f"${resultados[0][0]}")
    else:
        lbTotal = ttk.Label(frame, text="$0")    
    lbTotal.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    lbCantidadFactutas = ttk.Label(frame, text=f"Cantidad Facturas: ")
    lbCantidadFactutas.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    lbCantidadTotales = ttk.Label(frame, text=f"{resultados[0][1]}")
    lbCantidadTotales.grid(row=3, column=1, sticky="w", padx=5, pady=5)
    rendimientoGui.mainlopp()
menu()    