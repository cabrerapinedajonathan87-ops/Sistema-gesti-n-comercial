# src/reportes.py
import estructuras

def listado_general_productos():
    print("\n--- REPORTE: LISTADO DE PRODUCTOS ---")
    if not estructuras.lista_productos:
        print("No hay datos.")
        return
    for p in estructuras.lista_productos:
        print(f"Cód: {p['codigo']} | Nombre: {p['nombre']} | Inventario: {p['cantidad']} uds.")

def productos_bajo_minimo():
    print("\n--- REPORTE: PRODUCTOS EN STOCK CRÍTICO ---")
    encontrados = False
    for p in estructuras.lista_productos:
        if p["cantidad"] <= p["stock_minimo"]:
            print(f"🚨 Crítico: {p['nombre']} (Disponibles: {p['cantidad']} | Mínimo: {p['stock_minimo']})")
            encontrados = True
    if not encontrados:
        print("Ningún artículo está por debajo del stock de seguridad.")

def historial_ventas_procesadas():
    print("\n--- REPORTE: HISTORIAL COMPLETO DE VENTAS ---")
    if not estructuras.lista_ventas:
        print("No se han generado ventas en este período comercial.")
        return
    for v in estructuras.lista_ventas:
        print(f"Factura No: {v['numero_venta']} | Importe Neto: ${v['subtotal_general']:.2f} | IVA: ${v['iva']:.2f} | Total: ${v['total']:.2f}")

def total_ingresos_monetarios():
    print("\n--- REPORTE: TOTAL DE INGRESOS ---")
    total_acumulado = sum(v["total"] for v in estructuras.lista_ventas)
    print(f"💰 Sumatoria total capturada en cajas: ${total_acumulado:.2f}")

def producto_mas_vendido():
    print("\n--- REPORTE: PRODUCTO LÍDER DE VENTAS ---")
    if not estructuras.lista_ventas:
        print("Sin transacciones registradas.")
        return
        
    conteo_ventas = {}
    for v in estructuras.lista_ventas:
        for item in v["items"]:
            codigo = item["codigo"]
            conteo_ventas[codigo] = conteo_ventas.get(codigo, 0) + item["cantidad"]
            
    if not conteo_ventas:
        print("No hay unidades computadas.")
        return
        
    codigo_ganador = max(conteo_ventas, key=conteo_ventas.get)
    unidades_ganadoras = conteo_ventas[codigo_ganador]
    
    nombre_producto = "Eliminado/Inactivo"
    for p in estructuras.lista_productos:
        if p["codigo"] == codigo_ganador:
            nombre_producto = p["nombre"]
            break
            
    print(f"🏆 El artículo más vendido es '{nombre_producto}' (Código: {codigo_ganador}) con {unidades_ganadoras} unidades colocadas.")

def valor_total_inventario():
    print("\n--- REPORTE: EVALUACIÓN DE INVENTARIO EN BODEGA ---")
    capital_total = sum(p["precio"] * p["cantidad"] for p in estructuras.lista_productos)
    print(f"📈 Valor total de la mercancía a precio de venta: ${capital_total:.2f}")

def promedio_ventas_periodo():
    print("\n--- REPORTE: PROMEDIO DE FACTURACIÓN ---")
    if not estructuras.lista_ventas:
        print("Promedio de facturación actual: $0.00 (No hay registros)")
        return
    total_acumulado = sum(v["total"] for v in estructuras.lista_ventas)
    promedio = total_acumulado / len(estructuras.lista_ventas)
    print(f"📊 Ticket promedio por orden de compra: ${promedio:.2f} (Basado en {len(estructuras.lista_ventas)} ventas)")