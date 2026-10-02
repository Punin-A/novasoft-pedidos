# NovaSoft Pedidos

Sistema de pedidos de NovaSoft con cálculo de totales y pruebas automatizadas.

## Ejecución local

```bash
python app.py
python -m unittest -v
```

## Integración continua

El workflow de GitHub Actions se encuentra en `.github/workflows/ci.yml`. Se
ejecuta al realizar un `push` o abrir un `pull request` hacia `main`, y también
permite ejecución manual.

El pipeline realiza las siguientes actividades:

1. Descarga el repositorio.
2. Configura Python 3.13.
3. Compila los archivos Python.
4. Ejecuta la aplicación.
5. Ejecuta las pruebas automatizadas.
6. Genera y publica el artefacto `reporte-pruebas`.

El reporte se descarga desde la sección **Artifacts** de la ejecución en la
pestaña **Actions**. El flujo completo se encuentra en
[DIAGRAMA-CI.md](DIAGRAMA-CI.md).
