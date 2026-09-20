# Architecture

## Overview
El sistema es una aplicación local de interfaz de línea de comandos (CLI) escrita en Python. Su propósito es procesar consultas de búsqueda (por nombre o correo electrónico) enviadas por el usuario en la terminal, buscar coincidencias en un archivo JSON local y devolver los resultados formateados en pantalla.

## Components
1. **CLI Layer (`main.py` o módulo de entrada):** Maneja los argumentos de la terminal y muestra los resultados.
2. **Search Engine (`search_logic.py`):** Contiene las reglas de validación y la lógica de filtrado (case-insensitive, limpieza de espacios).
3. **Data Repository (`data_access.py`):** Encargado de abrir, leer y cargar la información del archivo `customers.json`.

## Responsibilities
- **CLI Layer:** Solo debe preocuparse por leer lo que el usuario escribe y hacer `print` de los resultados o errores. No debe buscar datos.
- **Search Engine:** Recibe el término, valida que tenga >= 2 caracteres y filtra la lista de clientes.
- **Data Repository:** Aísla el acceso al sistema de archivos. Maneja errores si el archivo JSON no existe o está corrupto.

## Data Flow
```mermaid
flowchart TD
    A[Usuario ejecuta CLI] --> B{CLI lee argumento}
    B -->|Término inválido| C[Mostrar Error: >= 2 caracteres]
    B -->|Término válido| D[Search Engine]
    D --> E[Data Repository]
    E --> F[(customers.json)]
    F --> E
    E -->|Devuelve Lista Clientes| D
    D -->|Filtra coincidencias| G{¿Hay resultados?}
    G -->|Sí| H[CLI imprime tabla/lista de clientes]
    G -->|No| I[CLI imprime mensaje 'Sin resultados']