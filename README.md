# Sistema de Gestión Comercial en Python

Sistema modular de consola para la gestión integral de productos, control de ventas, inventario y reportes estadísticos. Desarrollado como proyecto final para la asignatura de Algoritmos y Estructuras de Datos (Ingeniería en Sistemas).

## 🚀 Características
- **Módulo de Productos:** Registro, consulta, modificación y desactivación lógica de artículos.
- **Módulo de Ventas:** Procesamiento de transacciones comerciales con desglose de IVA (12%) e historial de salidas.
- **Control de Inventarios:** Monitoreo de existencias, reabastecimiento en bodega y alertas de stock crítico.
- **Reportes y Estadísticas:** Resumen numérico de ingresos, análisis de productos más vendidos, promedio de facturación y valoración comercial de bodega.
- **Persistencia de Datos:** Almacenamiento local mediante archivos de texto plano (`.txt`).

## 📁 Estructura del Proyecto
```text
sistema_comercial/
├── src/
│   ├── main.py
│   ├── estructuras.py
│   ├── archivos.py
│   ├── productos.py
│   ├── ventas.py
│   ├── inventario.py
│   └── reportes.py
├── productos.txt
├── ventas.txt
├── movimientos.txt
└── README.md
