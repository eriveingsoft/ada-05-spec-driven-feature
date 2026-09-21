# Reflexión Final - ADA-05

**1. ¿Qué diferencia hay entre requirement, specification y prompt?**
* **Requirement:** Es lo que el negocio o el usuario necesita (el "qué"). Por ejemplo: "Quiero poder buscar clientes". 
* **Specification:** Es cómo se va a medir y comprobar técnicamente que ese requerimiento funciona (el "cómo se valida"). Por ejemplo: "Si busco 'a', debe devolver clientes con 'a' ordenados alfabéticamente en menos de 500ms".
* **Prompt:** Es la orden textual que le doy al agente de IA para que escriba el código basándose en las dos anteriores, estableciendo sus límites.

**2. ¿Qué información fue indispensable antes de programar?**
Fue absolutamente necesario tener definidos los documentos `REQUIREMENTS.md`, `SPEC.md` y `ARCHITECTURE.md`. Sin una base clara sobre qué reglas de negocio se iban a aplicar y qué escenarios se iban a probar, el agente de IA hubiera inventado funcionalidades a su criterio.

**3. ¿Qué decisiones debieron resolverse antes de programar?**
Tuvimos que resolver las restricciones tecnológicas (como que solo se usaría Python y un JSON local sin bases de datos externas) y definir los criterios de validación exactos, como el límite mínimo de 2 caracteres y la sanitización de símbolos extraños para evitar inyecciones.

**4. ¿Qué errores evitó SPEC.md?**
Evitó que la IA "alucinara" e inventara reglas. Como el archivo de especificación contenía escenarios de prueba muy exactos (TS-01 a TS-05), la IA se vio obligada a programar el código necesario para que las pruebas pasaran, evitando que cambiara los mensajes de error o añadiera datos innecesarios.

**5. ¿Qué problema evita separar REQUIREMENTS.md de SPEC.md?**
Evita que las reglas del negocio se contaminen con detalles técnicos. Al separarlos, un usuario o cliente puede leer los requerimientos de forma sencilla, mientras que los desarrolladores (o el agente de IA) consultan la especificación para saber exactamente cómo codificar y configurar las pruebas automatizadas (en este caso con `pytest`).

**6. ¿Qué papel tuvo AGENTS.md?**
Funcionó como un "manual de comportamiento" para la IA. Le dio contexto sobre su rol, limitó sus acciones y sirvió como guía para los prompts que le envié, asegurando que el agente supiera que no tenía permitido alterar los requerimientos de negocio.

**7. ¿Qué cambió durante la revisión humana?**
Durante mi revisión, evalué las propuestas técnicas que la IA tomó por iniciativa propia ante espacios ambiguos. Por ejemplo, validé y aprobé el uso de las librerías `unicodedata` y `argparse`, asegurándome de que cumplieran con el requerimiento sin romper la arquitectura planeada.

**8. ¿La arquitectura coincidió con el código final?**
Sí, se mantuvo intacta la separación de responsabilidades. La interfaz de usuario CLI (`main.py`), la lógica del negocio y búsqueda (`search_logic.py`) y el modelo y acceso a datos (`domain.py`, `data_access.py`) quedaron totalmente desacoplados.

**9. ¿Qué requisito fue más difícil de probar?**
El requisito no funcional NFR-03 (Latencia menor a 500 ms). Fue complejo porque obligó a diseñar una prueba automatizada que utilizara subprocesos para medir el tiempo real de ejecución de la consola de principio a fin, en lugar de solo probar funciones aisladas.

**10. ¿Qué mejorarías en tu proceso spec-driven?**
Para futuros proyectos, trataría de definir desde el diseño inicial qué librerías estándar me gustaría que se utilizaran (por ejemplo, definir explícitamente el uso de `argparse`). Esto ayudaría a reducir la ambigüedad técnica y le daría un camino aún más directo a la IA.

**11. ¿Por qué SPEC.md puede funcionar como contrato verificable sin duplicar los requisitos?**
Porque el SPEC.md toma el requerimiento humano y lo traduce en Criterios de Aceptación (AC) y Escenarios de Prueba (TS) que se pueden comprobar mediante código (Test-Driven Development). Si las pruebas automatizadas pasan, existe evidencia matemática de que el contrato de negocio se cumplió.

**12. ¿Qué decisiones importantes aparecen en tu AI Usage Log y cómo cambió tu criterio después de revisar las sugerencias de la IA?**
Una decisión clave fue cuando la IA sugirió usar `unicodedata` para la normalización (limpiar los acentos) en la búsqueda. Inicialmente, no consideré esta herramienta técnica en mi planeación, pero al ver la sugerencia de la IA, me di cuenta de que era la manera más limpia, profesional y estándar en Python para resolver el requisito "case-insensitive". Mi criterio cambió al confiar en herramientas nativas del lenguaje propuestas por el agente.