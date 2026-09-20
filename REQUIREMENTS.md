# Requirements Customer Search

## User Story
As a user,
I want to search customers by name or email,
so that I can quickly find the customer record I need.

## Functional Requirements
FR-01: El sistema debe permitir realizar búsquedas proporcionando el nombre completo del cliente o una subcadena (fragmento) del nombre, sujeta a la validación de longitud mínima definida en FR-04.
FR-02: El sistema debe permitir realizar búsquedas proporcionando el correo electrónico completo del cliente o una subcadena (fragmento) del correo, sujeta a la validación de longitud mínima definida en FR-04.
FR-03: La funcionalidad de búsqueda debe ignorar las diferencias entre letras mayúsculas y minúsculas (case-insensitive) para maximizar los resultados.
FR-04: El sistema debe validar que la cadena de texto de búsqueda proporcionada por el usuario no esté vacía y contenga un mínimo estricto de 2 caracteres.
FR-05: Al encontrar coincidencias, el sistema debe devolver un objeto de respuesta con los datos de los clientes encontrados (incluyendo al menos ID, nombre y correo electrónico).
FR-06: Si la búsqueda no arroja ningún resultado, el sistema debe devolver una lista vacía y/o un mensaje claro indicando que no se encontraron coincidencias.

## Non-Functional Requirements
NFR-01: El sistema debe desarrollarse utilizando Python 3.11+ y ejecutarse en un entorno local.
NFR-02: La persistencia y lectura de los datos debe manejarse exclusivamente a través de un archivo JSON local o en memoria, sin utilizar bases de datos externas.
NFR-03: Las pruebas automatizadas del sistema deben implementarse utilizando el framework pytest.

## Open Questions
Q-01: ¿Se debe establecer un límite en el número máximo de registros devueltos si la búsqueda parcial coincide con demasiados clientes a la vez?
Q-02: ¿El sistema debería crear automáticamente un archivo JSON con datos falsos de prueba si detecta que el archivo no existe al momento de ejecutarse?

## Constraints / Assumptions
C-01: Constraint: El desarrollo debe realizarse desde cero, empleando únicamente herramientas gratuitas (Antigravity CLI) y sin requerir APIs de pago.
A-01: Assumption: Se asume que los correos electrónicos dentro del origen de datos (JSON) actuarán como identificadores únicos y no existirán dos clientes con el mismo correo.