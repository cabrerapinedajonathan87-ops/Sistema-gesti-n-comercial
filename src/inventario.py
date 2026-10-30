# src/inventario.py
import datetime
import estructuras
import archivos

def consultar_existencias():
    print("\n--- CONTROL DE EXISTENCIAS ---")
    if not estructuras.lista_productos:
        print("No existen registros.")
        return
    for p in estructuras.lista_productos:
        print(f"Producto: {p['nombre']} (Cód: {p['codigo']}) | Existencia en Bodega: {p['cantidad']}")

def registrar_entrada():
    print("\n--- REGISTRAR ENTRADA DE MERCANCÍA ---")
    codigo = input("Ingrese el código del producto para reabastecer: ").strip()
    
    for p in estructuras.lista_productos:
        if p["codigo"] == codigo:
            try:
                cantidad = int(input(f"Cantidad que entra para '{p['nombre']}': "))
                if cantidad <= 0:
                    print("❌ Error: La cantidad ingresada debe ser mayor que cero.")
                    return
                descripcion = input("Descripción del movimiento: ").strip() or "Reabastecimiento regular"
            except ValueError:
                print("❌ Error: Formato numérico incorrecto.")
                return
                
            p["cantidad"] += cantidad
            
            movimiento = {
                "fecha": str(datetime.date.today()),
                "codigo": codigo,
                "tipo": "ENTRADA",
                "cantidad": cantidad,
                "descripcion": descripcion
            }
            estructuras.historial_movimientos.append(movimiento)
            archivos.guardar_todo()
            print(f"✅ Inventario actualizado. Stock actual: {p['cantidad']}")
            return
    print("❌ El código de producto ingresado no existe.")

def alertar_stock_minimo():
    print("\n--- ALERTA DE STOCK MÍNIMO ---")
    alerta_activa = False
    for p in estructuras.lista_productos:
        if p["cantidad"] <= p["stock_minimo"]:
            print(f"⚠️ ALERTA: El producto '{p['nombre']}' (Cód: {p['codigo']}) tiene {p['cantidad']} unidades. (Mínimo requerido: {p['stock_minimo']})")
            alerta_activa = True
    if not alerta_activa:
        print("✅ Todos los productos operan con inventario seguro por encima del stock mínimo.")

def consultar_historial_movimientos():
    print("\n--- HISTORIAL DE MOVIMIENTOS DE BODEGA ---")
    if not estructuras.historial_movimientos:
        print("No se registran movimientos históricos en los archivos.")
        return
    for m in estructuras.historial_movimientos:
        print(f"Fecha: {m['fecha']} | Cód: {m['codigo']} | Tipo: {m['tipo']} | Cantidad: {m['cantidad']} | Motivo: {m['descripcion']}")