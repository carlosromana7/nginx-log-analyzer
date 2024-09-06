# Analizador de Logs de Nginx

Este proyecto es un analizador de logs de Nginx que procesa los archivos de registro y presenta los datos en un dashboard interactivo. Utiliza Docker para facilitar la implementación y Python para el procesamiento de logs y la generación del dashboard.

## Características

- Análisis de logs de Nginx en tiempo real
- Dashboard interactivo con métricas clave:
  - Total de solicitudes
  - IPs únicas
  - Tráfico total
  - Hora pico
- Visualizaciones gráficas:
  - Top 5 IPs
  - Distribución de códigos de estado HTTP
  - Top 5 rutas más accedidas
  - Top 5 User Agents
  - Top 5 nombres de servidores

## Tecnologías utilizadas

- Docker y Docker Compose para containerización
- Python para el procesamiento de logs
- Flask para el servidor web
- HTML y JavaScript para el frontend del dashboard

## Cómo usar

1. Clona este repositorio
2. Asegúrate de tener Docker y Docker Compose instalados
3. Ejecuta `docker-compose up --build` en la raíz del proyecto
4. Accede al dashboard en `http://localhost:5000`

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de enviar un pull request.

## Licencia

Este proyecto está bajo una licencia personalizada creada por [Carlos Alfredo Romaña Tuesta]. Todos los derechos reservados. El uso, distribución o modificación de este código está estrictamente prohibido sin permiso explícito del autor.
