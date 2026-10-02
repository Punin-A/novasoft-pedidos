# Diagrama de integración continua

```mermaid
flowchart TD
    A[Desarrollador modifica el código] --> B[Commit y push a main]
    B --> C[GitHub Actions inicia el pipeline]
    C --> D[Descargar repositorio]
    D --> E[Configurar Python 3.13]
    E --> F[Compilar archivos Python]
    F --> G[Ejecutar la aplicación]
    G --> H[Ejecutar pruebas unittest]
    H --> I[Generar reporte de pruebas]
    I --> J[Publicar reporte como artefacto]
    J --> K{Resultado del pipeline}
    K -->|Correcto| L[Pipeline exitoso]
    K -->|Error| M[Pipeline fallido]
```

El pipeline se ejecuta automáticamente con cada `push` o `pull request` dirigido
a la rama `main`. También puede iniciarse manualmente desde la pestaña
**Actions** de GitHub mediante la opción **Run workflow**.
