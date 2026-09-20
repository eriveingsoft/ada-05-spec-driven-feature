# Customer Search CLI

Buscador de clientes por línea de comandos (CLI) implementado en Python bajo el enfoque Spec-Driven Development (ADA-05). Permite filtrar clientes por nombre o correo electrónico a partir de un origen de datos local JSON, garantizando validaciones de entrada, insensibilidad a mayúsculas/acentos y ordenamiento alfabético.

---

## Requisitos Previos

* **Python:** Versión 3.11 o superior.
* **pytest:** Para la ejecución de pruebas automatizadas.

---

## Instalación de Dependencias

El proyecto utiliza la biblioteca estándar de Python para la lógica de negocio y persistencia. Para ejecutar las pruebas automatizadas, asegúrate de tener instalado `pytest`:

```bash
pip install pytest
```

---

## Estructura del Proyecto

```text
ada-05-spec-driven-feature/
│
├── customers.json          # Origen de datos local con clientes
├── pytest.ini              # Configuración de pytest y pythonpath
│
├── src/                    # Código fuente de la aplicación
│   ├── __init__.py
│   ├── domain.py           # Modelo de dominio (Customer)
│   ├── data_access.py      # Repositorio de lectura y parseo de JSON
│   ├── search_logic.py     # Motor de búsqueda, validaciones y filtros
│   └── main.py             # Interfaz de línea de comandos (CLI)
│
└── tests/                  # Suite de pruebas automatizadas
    ├── __init__.py
    ├── test_setup.py       # Validación de estructura y datos de prueba
    ├── test_domain.py      # Pruebas del modelo de dominio y repositorio
    └── test_search.py      # Pruebas del buscador, validaciones y CLI
```

---

## Instrucciones de Uso (CLI)

El punto de entrada principal es `src/main.py`. Puede ejecutarse directamente indicando el término de búsqueda de las siguientes maneras:

### 1. Búsqueda por argumento posicional
Busca coincidencias parciales o exactas tanto en el **nombre** como en el **correo electrónico**:

```bash
python src/main.py maria
```

### 2. Búsqueda específica por nombre (`--name`)
Filtra únicamente por el nombre del cliente:

```bash
python src/main.py --name ma
```

### 3. Búsqueda específica por correo (`--email`)
Filtra únicamente por la dirección o dominio de correo electrónico:

```bash
python src/main.py --email gmail
```

### 4. Búsqueda con bandera general (`-q` o `--query`)
```bash
python src/main.py -q "José"
```

---

## Reglas de Búsqueda y Validación

* **Insensibilidad a mayúsculas y acentos:** Las búsquedas ignoran mayúsculas y diacríticos (ej. buscar `jose` devolverá `José Pérez`, y buscar `MARIA` devolverá `Maria Gomez` y `María López`).
* **Longitud mínima:** Todo término debe contener al menos **2 caracteres válidos** tras eliminar espacios en blanco al inicio y al final (*trim*).
* **Caracteres permitidos:** Se permiten únicamente letras (incluyendo acentos y ñ), números, `@`, espacios y puntos (`.`). Cualquier intento de inyección o símbolo extraño es rechazado.
* **Ordenamiento:** Los resultados devueltos se presentan ordenados alfabéticamente por el nombre del cliente.

### Respuestas y Manejo de Errores
* Si la búsqueda tiene menos de 2 caracteres:
  ```text
  Error: El término de búsqueda debe tener al menos 2 caracteres válidos.
  ```
* Si la búsqueda no arroja resultados:
  ```text
  No se encontraron clientes para el término de búsqueda.
  ```
* Si se ingresan caracteres inválidos:
  ```text
  Error: El término de búsqueda contiene caracteres no permitidos. Solo se permiten letras, números, @, espacios y puntos.
  ```

---

## Ejecución de Pruebas Automatizadas

Para ejecutar la suite completa de pruebas unitarias y de integración:

```bash
python -m pytest -v
```

También es posible correr pruebas por módulo específico:

```bash
pytest tests/test_setup.py -v
pytest tests/test_domain.py -v
pytest tests/test_search.py -v
```