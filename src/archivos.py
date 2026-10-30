# src/archivos.py
import os
import estructuras

# Nombres de los archivos físicos de almacenamiento
ARCHIVO_PRODUCTOS = "productos.txt"
ARCHIVO_VENTAS = "ventas.txt"
ARCHIVO_MOVIMIENTOS = "movimientos.txt"

def guardar_todo():
    """Guarda todas las listas internas del sistema en los archivos de texto."""
    # 1. Guardar Productos
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as f:
        for p in estructuras.lista_productos:
            f.write(f"{p['codigo']}|{p['nombre']}|{p['categoria']}|{p['precio']}|{p['cantidad']}|{p['stock_minimo']}|{p['activo']}\n")
            
    # 2. Guardar Ventas
    with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as f:
        for v in estructuras.lista_ventas:
            items_str = ";".join([f"{item['codigo']},{item['cantidad']},{item['subtotal']}" for item in v['items']])
            f.write(f"{v['numero_venta']}|{v['subtotal_general']}|{v['iva']}|{v['total']}|{items_str}\n")
            
    # 3. Guardar Movimientos
    with open(ARCHIVO_MOVIMIENTOS, "w", encoding="utf-8") as f:
        for m in estructuras.historial_movimientos:
            f.write(f"{m['fecha']}|{m['codigo']}|{m['tipo']}|{m['cantidad']}|{m['descripcion']}\n")

def cargar_todo():
    """Carga los datos desde los archivos de texto hacia las listas en memoria."""
    # 1. Cargar Productos
    if os.path.exists(ARCHIVO_PRODUCTOS):
        estructuras.lista_productos.clear()
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    partes = linea.split("|")
                    p = {
                        "codigo": partes[0],
                        "nombre": partes[1],
                        "categoria": partes[2],
                        "precio": float(partes[3]),
                        "cantidad": int(partes[4]),
                        "stock_minimo": int(partes[5]),
                        "activo": partes[6] == "True"
                    }
                    estructuras.lista_productos.append(p)
                    
    # 2. Cargar Ventas
    if os.path.exists(ARCHIVO_VENTAS):
        estructuras.lista_ventas.clear()
        with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    partes = linea.split("|")
                    v = {
                        "numero_venta": int(partes[0]),
                        "subtotal_general": float(partes[1]),
                        "iva": float(partes[2]),
                        "total": float(partes[3]),
                        "items": []
                    }
                    if partes[4]:
                        detalles = partes[4].split(";")
                        for d in detalles:
                            if d:
                                sub_partes = d.split(",")
                                item = {
                                    "codigo": sub_partes[0],
                                    "cantidad": int(sub_partes[1]),
                                    "subtotal": float(sub_partes[2])
                                }
                                v["items"].append(item)
                    estructuras.lista_ventas.append(v)
                    
    # 3. Cargar Movimientos
    if os.path.exists(ARCHIVO_MOVIMIENTOS):
        estructuras.historial_movimientos.clear()
        with open(ARCHIVO_MOVIMIENTOS, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    partes = linea.split("|")
                    m = {
                        "fecha": partes[0],
                        "codigo": partes[1],
                        "tipo": partes[2],
                        "cantidad": int(partes[3]),
                        "descripcion": partes[4]
                    }
                    estructuras.historial_movimientos.append(m)