# Tasks

## T-01 Project setup
- **Goal:** Inicializar la estructura del proyecto en Python, configurar `pytest` y crear el archivo `customers.json` con datos ficticios para las pruebas.
- **Files:** `customers.json`, `src/__init__.py`, `tests/__init__.py`.
- **Acceptance:** El archivo JSON existe con al menos 5 clientes (incluyendo casos con correos @gmail.com y variaciones de nombres como "Maria"). El entorno puede leer el archivo.
- **Verification:** Ejecutar un script temporal en Python que lea y haga print del contenido de `customers.json`.

## T-02 Domain model
- **Goal:** Crear la estructura de datos que representará a un cliente en memoria, asegurando que contenga `id`, `name` y `email`.
- **Files:** `src/data_access.py` (o `src/domain.py`).
- **Acceptance:** El sistema puede convertir los diccionarios leídos del archivo JSON en objetos o diccionarios tipados de Python de manera segura.
- **Verification:** Escribir y ejecutar una prueba en `pytest` que instancie un cliente exitosamente.

## T-03 Search logic
- **Goal:** Implementar el motor de búsqueda que filtre clientes por nombre o correo, ignorando mayúsculas/minúsculas y ordenando los resultados alfabéticamente por nombre.
- **Files:** `src/search_logic.py`, `tests/test_search.py`.
- **Acceptance:** La función de búsqueda retorna la lista correcta de clientes según los escenarios TS-01 y TS-02 definidos en `SPEC.md`.
- **Verification:** Ejecutar `pytest -v` para confirmar que las pruebas de la lógica de filtrado pasan.

## T-04 Validation and errors
- **Goal:** Implementar las reglas de validación (mínimo 2 caracteres tras limpiar espacios) y los mensajes de error estructurales requeridos si no hay resultados o la entrada es inválida.
- **Files:** `src/search_logic.py`, `tests/test_search.py`.
- **Acceptance:** Las búsquedas de 1 carácter arrojan el error de longitud. Las búsquedas sin coincidencias devuelven el mensaje informativo correspondiente (TS-03 y TS-04 de `SPEC.md`).
- **Verification:** Ejecutar `pytest -v` verificando que las excepciones y los mensajes de error se disparen correctamente.

## T-05 CLI Integration & Tests
- **Goal:** Construir la interfaz de línea de comandos para que el usuario pueda enviar argumentos (ej. `--name` o `--email`) y asegurar la cobertura final de pruebas.
- **Files:** `src/main.py`, `tests/test_search.py`.
- **Acceptance:** El usuario puede ejecutar el buscador desde la terminal. Todos los Criterios de Aceptación (AC-01 al AC-04) tienen una prueba automatizada correspondiente.
- **Verification:** Ejecutar manualmente el programa en la terminal (ej. `python src/main.py --name ma`) y ejecutar la suite completa de `pytest -v`.

## T-06 Documentation
- **Goal:** Actualizar el archivo README principal del repositorio con las instrucciones exactas de uso.
- **Files:** `README.md`.
- **Acceptance:** El README documenta cómo instalar dependencias, cómo ejecutar una búsqueda y cómo correr las pruebas automatizadas.
- **Verification:** Leer el README y replicar los comandos copiándolos y pegándolos en la terminal para asegurar que funcionan sin errores.