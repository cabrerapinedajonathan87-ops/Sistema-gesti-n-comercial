# src/ventas.py
import datetime
import estructuras
import archivos

def registrar_venta():
    print("\n--- NUEVA TRANSACCIÓN DE VENTA ---")
    if not estructuras.lista_productos:
        print("❌ No hay productos en la tienda para poder efectuar una venta.")
        return
        
    carrito = []
    subtotal_general = 0.0
    
    while True:
        codigo = input("Ingrese el código del producto a vender (o 'FIN' para procesar): ").strip()
        if codigo.upper() == "FIN":
            break
            
        producto_encontrado = None
        for p in estructuras.lista_productos:
            if p["codigo"] == codigo:
                producto_encontrado = p
                break
                
        if not producto_encontrado:
            print("❌ El código ingresado no coincide con ningún producto.")
            continue
            
        if not producto_encontrado["activo"]:
            print("❌ Este producto se encuentra desactivado para la venta.")
            continue
            
        try:
            cantidad = int(input(f"¿Cuántas unidades de '{producto_encontrado['nombre']}' desea vender?: "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser un entero positivo.")
                continue
            if cantidad > producto_encontrado["cantidad"]:
                print(f"❌ Inventario insuficiente. Stock actual disponible: {producto_encontrado['cantidad']}")
                continue
        except ValueError:
            print("❌ Entrada incorrecta. Debe ingresar un valor numérico entero.")
            continue
            
        subtotal_item = producto_encontrado["precio"] * cantidad
        
        carrito.append({
            "codigo": codigo,
            "cantidad": cantidad,
            "subtotal": subtotal_item,
            "ref_producto": producto_encontrado
        })
        print(f"➕ Añadido al carrito: {producto_encontrado['nombre']} x{cantidad} - Subtotal: ${subtotal_item:.2f}")
        
    if not carrito:
        print("⚠️ Venta cancelada debido a que no se ingresaron artículos.")
        return
        
    for item in carrito:
        subtotal_general += item["subtotal"]
        
    iva = subtotal_general * 0.12
    total = subtotal_general + iva
    
    numero_venta = len(estructuras.lista_ventas) + 1
    
    for item in carrito:
        p = item["ref_producto"]
        p["cantidad"] -= item["cantidad"]
        
        movimiento = {
            "fecha": str(datetime.date.today()),
            "codigo": p["codigo"],
            "tipo": "SALIDA (VENTA)",
            "cantidad": item["cantidad"],
            "descripcion": f"Venta registrada con el folio No. {numero_venta}"
        }
        estructuras.historial_movimientos.append(movimiento)
        
    datos_venta = {
        "numero_venta": numero_venta,
        "subtotal_general": subtotal_general,
        "iva": iva,
        "total": total,
        "items": [{"codigo": x["codigo"], "cantidad": x["cantidad"], "subtotal": x["subtotal"]} for x in carrito]
    }
    
    estructuras.lista_ventas.append(datos_venta)
    archivos.guardar_todo()
    
    print("\n=======================================")
    print(f"         COMPROBANTE DE VENTA No. {numero_venta}")
    print("=======================================")
    print(f"Subtotal Neto:     ${subtotal_general:.2f}")
    print(f"IVA (12%):         ${iva:.2f}")
    print(f"Total a Pagar:     ${total:.2f}")
    print("=======================================")
    print("✅ La transacción comercial fue almacenada con éxito.")