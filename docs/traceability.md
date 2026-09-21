| Requirement | SPEC / AC | Task | Files | Test | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FR-01 | AC-01 / TS-01 | T-03 | `search_logic.py` | `test_search_by_name_exact_and_accent_insensitive_ts_01` | Done | Búsqueda por nombre implementada; ignora mayúsculas y acentos. |
| FR-02 | AC-02 / TS-02 | T-03 | `search_logic.py` | `test_search_by_email_domain_partial_ts_02` | Done | Búsqueda parcial por correo electrónico (ej. por dominio) validada. |
| FR-03 | TS-05 | T-03 | `search_logic.py` | `test_search_results_alphabetical_ordering_ts_05` | Done | Los resultados se ordenan alfabéticamente de forma estricta. |
| FR-04 | AC-03 / TS-03 | T-04 | `search_logic.py` | `test_search_rejects_empty_or_single_char_ts_03` | Done | Validación activa: rechaza menos de 2 caracteres y bloquea símbolos raros. |
| FR-05 | AC-04 / TS-04 | T-04 | `search_logic.py` | `test_search_no_results_ts_04_ac_04` | Done | Mensaje informativo exacto devuelto al no encontrar coincidencias. |
| FR-06 | N/A | T-02 | `domain.py`, `data_access.py` | `test_instantiate_customer_successfully` | Done | Estructura inmutable del cliente (`id`, `name`, `email`) y carga segura. |
| NFR-01 | N/A | T-01 | `test_setup.py` | `test_customers_json_exists_and_is_valid` | Done | Entorno base configurado correctamente para las pruebas (Python 3.11+). |
| NFR-02 | N/A | T-01 | `customers.json` | `test_customers_json_exists_and_is_valid` | Done | Archivo local JSON creado con los datos de prueba semilla. |
| NFR-03 | AC-05 | T-05 | `test_search.py` | `test_search_execution_latency_ac_05` | Done | Latencia verificada desde la CLI; ejecución completa en < 500 ms. |