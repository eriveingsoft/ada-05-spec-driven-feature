# Agent Report 

## Agent / Version 
Antigravity CLI (con modelo Gemini)

## Initial Context 
El repositorio contaba exclusivamente con los documentos fundacionales de diseño: `REQUIREMENTS.md`, `SPEC.md`, `ARCHITECTURE.md` y `TASKS.md`. No existía código fuente previo, por lo que el agente partió de un entorno limpio para iniciar el ciclo de Spec-Driven Development.

## Task Sequence 

### T-01 
**What the agent did:** Leyó la especificación del proyecto, configuró el archivo `pytest.ini` para el marco de pruebas y creó el archivo de persistencia `customers.json` poblándolo con 6 registros semilla que incluían casos borde (acentos, dominios @gmail).
**Human review:** Se autorizó la creación de los archivos y se validó en la terminal que el JSON tuviera la estructura esperada por los criterios de aceptación.
**Tests:** 1 prueba pasando (`test_setup.py`).

### T-02 
**What the agent did:** Implementó el modelo inmutable `Customer` utilizando `dataclasses` en `domain.py`. Desarrolló la lógica de lectura del archivo JSON en `data_access.py` incluyendo manejo de excepciones para archivos inexistentes o corruptos.
**Human review:** Se verificó que el manejo de errores cumpliera con buenas prácticas y no expusiera trazas (stacktraces) crudas al usuario.
**Tests:** 8 pruebas pasando en la suite (`test_domain.py`).

### T-03 
**What the agent did:** Codificó el motor de búsqueda en `search_logic.py`. Para cumplir el requisito case-insensitive, utilizó la librería `unicodedata` estandarizando el texto (NFD) para omitir acentos.
**Human review:** Se aceptó la propuesta técnica del agente (uso de `unicodedata`) y se aprobó una refactorización en la prueba automatizada del ordenamiento alfabético para hacerla más estricta.
**Tests:** 15 pruebas pasando en total.

### T-04 
**What the agent did:** Implementó reglas de validación defensivas. Exigió una longitud mínima de 2 caracteres (tras hacer strip) y bloqueó activamente símbolos especiales (;, $, <) para prevenir inyección de comandos.
**Human review:** Se comprobó minuciosamente que los mensajes de error textuales devueltos por el sistema fueran idénticos letra por letra a los estipulados en el `SPEC.md`.
**Tests:** 29 pruebas pasando en total, asegurando escenarios vacíos o cortos.

### T-05 
**What the agent did:** Construyó la interfaz de línea de comandos en `main.py` empleando la librería `argparse` para estructurar las banderas `--name`, `--email` y `-q`. 
**Human review:** Se verificó la matriz de cobertura reportada por el agente y se validó el requisito no funcional de latencia, comprobando que las respuestas tomaran menos de 500 ms.
**Tests:** 37 pruebas pasando en total.

### T-06
**What the agent did:** Actualizó el documento `README.md` detallando la instalación, el árbol de directorios y los comandos exactos de ejecución.
**Human review:** Se corrieron manualmente los comandos en PowerShell para comprobar que la documentación coincidiera 100% con el software generado.
**Tests:** N/A (Tarea de documentación).

## Problems Encountered 
Hubo ambigüedad técnica inicial respecto a cómo abordar exactamente la insensibilidad de mayúsculas/acentos y con qué librería construir la consola, ya que esto no estaba definido en el requerimiento.

## Human Interventions 
Se establecieron prompts restrictivos y estandarizados antes de iniciar las tareas (ej. "Do not invent business requirements") para limitar la autonomía del agente. Se evaluaron y aprobaron las sugerencias técnicas de la IA (`unicodedata` y `argparse`) porque resolvían la ambigüedad sin romper la arquitectura establecida.

## Requirement / Specification Changes 
No hubo alteraciones en los requerimientos de negocio (`REQUIREMENTS.md`). Únicamente se precisó técnicamente en la revisión humana que el término "case-insensitive" abarcaría explícitamente la omisión de acentos. El SPEC.md funcionó correctamente como contrato inmutable; aprobado por Roberto.

## Final Verification 
El producto de software final es completamente funcional a través de CLI, está desacoplado lógicamente y pasa de forma exitosa y veloz (aprox. 0.3 segundos) una batería de 37 pruebas automatizadas con `pytest`. Cumple al 100% con la trazabilidad planificada.

## Lessons Learned 
Mantener los requisitos funcionales separados de las especificaciones técnicas cómo probarlo es vital para el desarrollo con IA. Cuando el `SPEC.md` contiene escenarios de prueba cerrados y estrictos, se elimina el riesgo de que el agente autónomo alucine funcionalidades o evada validaciones de seguridad.