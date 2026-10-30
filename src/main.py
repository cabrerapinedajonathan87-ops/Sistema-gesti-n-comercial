# src/main.py
import os
import archivos
import productos
import inventario
import ventas
import reportes

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        print("\n=======================================")
        print("     SISTEMA DE GESTIÓN COMERCIAL      ")
        print("=======================================")
        print("1. Gestión de Productos 📦")
        print("2. Registro de Ventas 🛒")
        print("3. Control de Inventarios 🏢")
        print("4. Reportes y Estadísticas 📊")
        print("5. Salir del Sistema ❌")
        print("=======================================")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            limpiar_pantalla()
            while True:
                print("\n--- [MÓDULO 1: GESTIÓN DE PRODUCTOS] ---")
                print("1. Registrar Producto")
                print("2. Consultar Producto por Código")
                print("3. Mostrar Listado Completo")
                print("4. Modificar Producto")
                print("5. Desactivar Producto")
                print("6. Regresar al Menú Principal")
                sub = input("Opción: ").strip()
                if sub == "1": productos.registrar_producto()
                elif sub == "2": productos.consultar_producto_por_codigo()
                elif sub == "3": productos.mostrar_listado_productos()
                elif sub == "4": productos.modificar_producto()
                elif sub == "5": productos.desactivar_producto()
                elif sub == "6": break
                else: print("❌ Opción inválida.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()
                
        elif opcion == "2":
            limpiar_pantalla()
            ventas.registrar_venta()
            input("\nPresione Enter para regresar al menú principal...")
            limpiar_pantalla()
            
        elif opcion == "3":
            limpiar_pantalla()
            while True:
                print("\n--- [MÓDULO 3: CONTROL DE INVENTARIOS] ---")
                print("1. Consultar Existencias")
                print("2. Registrar Entrada de Mercancía")
                print("3. Verificar Alertas de Stock Mínimo")
                print("4. Ver Historial de Movimientos")
                print("5. Regresar al Menú Principal")
                sub = input("Opción: ").strip()
                if sub == "1": inventario.consultar_existencias()
                elif sub == "2": inventario.registrar_entrada()
                elif sub == "3": inventario.alertar_stock_minimo()
                elif sub == "4": inventario.consultar_historial_movimientos()
                elif sub == "5": break
                else: print("❌ Opción inválida.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()
                
        elif opcion == "4":
            limpiar_pantalla()
            while True:
                print("\n--- [MÓDULO 4: REPORTES Y ESTADÍSTICAS] ---")
                print("1. Listado General de Productos")
                print("2. Reporte de Stock Crítico")
                print("3. Historial de Ventas")
                print("4. Total de Ingresos")
                print("5. Producto Más Vendido")
                print("6. Valor Total del Inventario")
                print("7. Promedio de Ventas")
                print("8. Regresar al Menú Principal")
                sub = input("Opción: ").strip()
                if sub == "1": reportes.listado_general_productos()
                elif sub == "2": reportes.productos_bajo_minimo()
                elif sub == "3": reportes.historial_ventas_procesadas()
                elif sub == "4": reportes.total_ingresos_monetarios()
                elif sub == "5": reportes.producto_mas_vendido()
                elif sub == "6": reportes.valor_total_inventario()
                elif sub == "7": reportes.promedio_ventas_periodo()
                elif sub == "8": break
                else: print("❌ Opción inválida.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()
                
        elif opcion == "5":
            print("\nGuardando cambios de forma segura... Cierre exitoso del sistema. 👋")
            break
        else:
            print("\n❌ Opción no reconocida. Intente con números del 1 al 5.")
            input("Presione Enter para continuar...")
            limpiar_pantalla()

if __name__ == "__main__":
    archivos.cargar_todo()
    limpiar_pantalla()
    menu_principal()