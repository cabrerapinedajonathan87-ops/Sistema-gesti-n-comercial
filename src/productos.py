# src/productos.py
import estructuras
import archivos

def registrar_producto():
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    codigo = input("Ingrese el código del producto: ").strip()
    if not codigo:
        print("❌ Error: El código no puede estar vacío.")
        return
        
    for p in estructuras.lista_productos:
        if p["codigo"] == codigo:
            print("❌ Error: Código duplicado detectado.")
            return

    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría: ").strip()
    if not nombre or not categoria:
        print("❌ Error: Nombre y categoría son obligatorios.")
        return

    try:
        precio = float(input("Ingrese el precio de venta: "))
        cantidad = int(input("Ingrese la cantidad disponible inicial: "))
        stock_minimo = int(input("Ingrese el stock mínimo: "))
        
        if precio < 0 or cantidad < 0 or stock_minimo < 0:
            print("❌ Error: El precio y las cantidades no pueden ser negativos.")
            return
    except ValueError:
        print("❌ Error: Entrada de datos de tipo numérico incorrecta.")
        return

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad,
        "stock_minimo": stock_minimo,
        "activo": True
    }
    
    estructuras.lista_productos.append(nuevo_producto)
    archivos.guardar_todo()
    print(f"✅ Producto '{nombre}' registrado de forma exitosa.")

def consultar_producto_por_codigo():
    print("\n--- CONSULTAR PRODUCTO ---")
    codigo = input("Ingrese el código a buscar: ").strip()
    
    for p in estructuras.lista_productos:
        if p["codigo"] == codigo:
            estado = "Disponible" if p["activo"] else "Desactivado (No disponible para venta)"
            print(f"\n🔍 Producto Encontrado:\nCódigo: {p['codigo']}\nNombre: {p['nombre']}\nCategoría: {p['categoria']}")
            print(f"Precio: ${p['precio']:.2f}\nCantidad: {p['cantidad']}\nStock Mínimo: {p['stock_minimo']}\nEstado: {estado}")
            return
    print("❌ Producto no encontrado en el sistema.")

def mostrar_listado_productos():
    print("\n--- LISTADO GENERAL DE PRODUCTOS ---")
    if not estructuras.lista_productos:
        print("No existen productos registrados.")
        return
        
    for p in estructuras.lista_productos:
        estado = "OK" if p["activo"] else "DESACTIVADO"
        print(f"[{estado}] Cód: {p['codigo']} | {p['nombre']} | Cat: {p['categoria']} | ${p['precio']:.2f} | Stock: {p['cantidad']} (Min: {p['stock_minimo']})")

def modificar_producto():
    print("\n--- MODIFICAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a modificar: ").strip()
    
    for p in estructuras.lista_productos:
        if p["codigo"] == codigo:
            print(f"Modificando: {p['nombre']}")
            nuevo_nombre = input(f"Nuevo nombre [{p['nombre']}]: ").strip() or p['nombre']
            nueva_cat = input(f"Nueva categoría [{p['categoria']}]: ").strip() or p['categoria']
            
            try:
                precio_input = input(f"Nuevo precio [{p['precio']}]: ").strip()
                nuevo_precio = float(precio_input) if precio_input else p['precio']
                
                min_input = input(f"Nuevo stock mínimo [{p['stock_minimo']}]: ").strip()
                nuevo_min = int(min_input) if min_input else p['stock_minimo']
                
                if nuevo_precio < 0 or nuevo_min < 0:
                    print("❌ Error: Los valores no pueden ser negativos.")
                    return
            except ValueError:
                print("❌ Error: Entrada numérica no válida.")
                return
                
            p["nombre"] = nuevo_nombre
            p["categoria"] = nueva_cat
            p["precio"] = nuevo_precio
            p["stock_minimo"] = nuevo_min
            archivos.guardar_todo()
            print("✅ Producto modificado exitosamente.")
            return
    print("❌ Producto no encontrado.")

def desactivar_producto():
    print("\n--- DESACTIVAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a desactivar: ").strip()
    
    for p in estructuras.lista_productos:
        if p["codigo"] == codigo:
            p["activo"] = False
            archivos.guardar_todo()
            print(f"✅ El producto '{p['nombre']}' ha sido marcado como inactivo.")
            return
    print("❌ Producto no encontrado.")