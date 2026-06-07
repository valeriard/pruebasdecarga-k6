# Prueba de carga con k6 — Proyecto "k6-reto"

**Descripción**
- **Resumen:** Proyecto de ejemplo que contiene un test de login para k6.
- **Objetivo:** ejecutar pruebas de carga/funcionales usando k6 sobre el script provisto.

**Requisitos**
- **k6:** Instala k6 en tu sistema. Ejemplos:
  - Windows (chocolatey): `choco install k6`
  - macOS (Homebrew): `brew install k6`
  - Linux: sigue las instrucciones oficiales en https://k6.io/docs/

**Archivos**
- **login_test.js:** [login_test.js](login_test.js) — Script de k6 que contiene el escenario de login.
- **users.csv:** [users.csv](users.csv) — Archivo CSV con datos de usuarios (credenciales) usados por el test.

**Uso rápido**
- **Ejecutar prueba por defecto:**

  `k6 run login_test.js`

- **Ejecutar con usuarios virtuales y duración:**

  `k6 run --vus 50 --duration 30s login_test.js`

- **Guardar salida en JSON:**

  `k6 run --out json=results.json login_test.js`

**Notas sobre el CSV**
- El script espera que `users.csv` esté en el mismo directorio. Si el script usa `open()` o una ruta relativa, ajusta la ubicación del CSV o la ruta en el script.

**Consejos**
- Antes de lanzar pruebas de alta carga contra entornos reales, confirma con el equipo responsable del servicio.
- Revisa la salida de k6 para métricas clave: **http_req_duration**, **checks**, **errors**.

**Contribuciones**
- Abre issues o PRs con mejoras al script o al dataset. Añade ejemplos reproducibles.

**Licencia**
- Este repositorio usa la licencia MIT por defecto. Cambia según prefieras.

---

¿Quieres que añada un `package.json`, scripts de ejecución o ejemplos de CI para este test?
