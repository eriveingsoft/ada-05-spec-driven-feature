# Customer Search Feature

## Goal
Proveer un mecanismo eficiente y preciso para buscar clientes por nombre o correo electrónico dentro de un archivo local JSON, asegurando validaciones correctas y respuestas estructuradas.

## Requirements Covered
FR-01
FR-02
FR-03
FR-04
FR-05
FR-06
NFR-01
NFR-02
NFR-03

## Scope
Implementación de un buscador mediante una aplicación de consola (CLI) que lea un JSON local. Se incluye la lógica de búsqueda, las validaciones y el manejo de errores.

## Out of Scope
Creación de bases de datos, interfaces gráficas (GUI), APIs web o autenticación de usuarios.

## Domain Model
- **Customer:** Entidad con al menos tres campos: `id` (entero o string único), `name` (string) y `email` (string).

## Search Rules
- **Sensibilidad de acentos:** La búsqueda debe ignorar los acentos. Buscar "Jose" debe devolver "José" y viceversa.
- **Símbolos y espacios:** Los espacios en blanco al inicio o al final del término de búsqueda deben eliminarse (*trim*).
- **Orden de resultados:** Los resultados devueltos deben ordenarse alfabéticamente por el campo `name` (Nombre del cliente).
- Si la búsqueda coincide con un fragmento del nombre y también con el correo de clientes distintos, se deben devolver ambos resultados.

## Validation Rules
- La cadena de búsqueda, después de limpiarle los espacios (trim), debe tener una longitud >= 2 caracteres.
- La búsqueda no puede contener caracteres de inyección de comandos o símbolos especiales extraños (solo letras, números, @, espacios y puntos).

## Error Handling
- Si la búsqueda tiene menos de 2 caracteres: Imprimir el mensaje de error `Error: El término de búsqueda debe tener al menos 2 caracteres válidos.`
- Si la búsqueda es exitosa pero no arroja resultados: Imprimir el mensaje informativo `No se encontraron clientes para el término de búsqueda.`

## Acceptance Criteria
- AC-01: (Cubre FR-01, FR-03, FR-05) Buscar "maria" devuelve a "Maria Gomez" y "María López", ordenadas alfabéticamente.
- AC-02: (Cubre FR-02, FR-05) Buscar "@gmail" devuelve todos los clientes con correos de ese dominio.
- AC-03: (Cubre FR-04) Buscar "a" o un espacio vacío (" ") es rechazado con el error de longitud.
- AC-04: (Cubre FR-06) Buscar un término inexistente (ej. "XYZ999") devuelve el mensaje "No se encontraron clientes para el término de búsqueda."
- AC-05: (Cubre NFR-03) El sistema ejecuta la lectura del JSON y devuelve los resultados en la terminal en menos de 500 milisegundos.

## Test Scenarios
- **TS-01:** Búsqueda exacta por nombre (case y acentos ignorados).
- **TS-02:** Búsqueda parcial por dominio de correo electrónico.
- **TS-03:** Validar rechazo de búsqueda vacía o de 1 carácter.
- **TS-04:** Validar respuesta vacía (sin resultados) con término inexistente.
- **TS-05:** Validar correcto ordenamiento alfabético de los resultados devueltos.

## Constraints
- N/A. (Las restricciones ya están definidas en REQUIREMENTS.md, sección C-01).

## Open Questions
- N/A. (Resolvimos el mensaje de error y el límite de resultados dentro de este SPEC).