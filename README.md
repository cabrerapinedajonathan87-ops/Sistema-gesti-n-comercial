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


graph TD
    A[Inicio: Registrar Producto] --> B[Ingresar datos: ID, Nombre, Precio, Stock]
    B --> C{¿ID o Nombre ya existen?}
    C -- Sí --> D[Mostrar error: Producto ya registrado]
    D --> B
    C -- No --> E{¿Precio > 0 y Stock >= 0?}
    E -- No --> F[Mostrar error: Valores numéricos inválidos]
    F --> B
    E -- Sí --> G[Crear estructura del Producto]
    G --> H[Agregar a la lista en memoria]
    H --> I[Llamar a guardar_en_archivo]
    I --> J[Fin: Producto Registrado]
│   ├── inventario.py
│   └── reportes.py
├── productos.txt
├── ventas.txt
├── movimientos.txt
└── README.md

graph TD
    A[Inicio: Consultar / Modificar] --> B[Ingresar ID o Nombre del producto]
    B --> C{¿Producto encontrado en inventario?}
    C -- No --> D[Mostrar error: Producto no encontrado]
    D --> E{¿Desea reintentar?}
    E -- Sí --> B
    E -- No --> Z[Fin del Proceso]
    C -- Sí --> F[Mostrar detalles del Producto]
    F --> G{¿Desea modificar el producto?}
    G -- No --> Z
    G -- Sí --> H[Ingresar nuevos datos: Nombre, Precio, Stock]
    H --> I{¿Validación de precio y stock correcta?}
    I -- No --> J[Mostrar error: Datos inválidos]
    J --> H
    I -- Sí --> K[Actualizar datos del producto en memoria]
    K --> L[Persistir cambios en archivo]
    L --> Z

graph TD
    A[Inicio: Registrar Venta] --> B[Ingresar ID del producto a vender]
    B --> C{¿Producto existe?}
    C -- No --> D[Mostrar error: Producto inexistente]
    D --> Z[Fin de Venta]
    C -- Sí --> E[Ingresar Cantidad a vender]
    E --> F{¿Stock disponible >= Cantidad?}
    F -- No --> G[Mostrar error: Stock insuficiente]
    G --> Z
    F -- Sí --> H[Calcular Subtotal, IVA y Total]
    H --> I[Generar factura / comprobante de venta]
    I --> J[Descontar cantidad del Stock del producto]
    J --> K[Actualizar inventario.py]
    K --> L[Guardar registro de venta en archivo]
    L --> Z

graph TD
    A[Inicio: Actualizar Inventario] --> B[Cargar inventario desde archivo]
    B --> C{¿Transacción recibida?}
    C -- Entrada/Compra --> D[Sumar cantidad a Stock actual]
    C -- Salida/Venta --> E[Restar cantidad a Stock actual]
    D --> F[Verificar límite mínimo/máximo de Stock]
    E --> F
    F --> G[Actualizar estado en memoria]
    G --> H[Escribir actualización en archivo de persistencia]
    H --> I[Fin: Inventario Actualizado]

graph TD
    A[Inicio: Carga de Datos] --> B[Intentar abrir archivo de datos .json / .txt / .csv]
    B --> C{¿Existe el archivo?}
    C -- No --> D[Crear archivo nuevo con estructura vacía]
    D --> E[Retornar lista/diccionario vacío]
    C -- Sí --> F[Leer contenido del archivo]
    F --> G{¿Archivo corrupto o con sintaxis inválida?}
    G -- Sí --> H[Lanzar excepción y cargar respaldo / vaciar]
    G -- No --> I[Parsear contenido a objetos de memoria]
    H --> Z[Fin de Carga]
    I --> Z

graph TD
    A[Inicio: Generar Reporte] --> B[Seleccionar tipo: Ventas, Stock Bajo, Totales]
    B --> C[Leer datos desde inventario y ventas]
    C --> D{¿Existen registros para el reporte?}
    D -- No --> E[Mostrar mensaje: No hay datos disponibles]
    E --> Z[Fin de Reporte]
    D -- Sí --> F[Procesar cálculos: Totales, promedios, filtros]
    F --> G[Formatear salida: Consola / Archivo exportado]
    G --> H[Presentar o guardar reporte]
    H --> Z
