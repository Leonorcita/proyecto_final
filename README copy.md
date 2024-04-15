# Proyecto DevOps

Este proyecto implementa una API RESTful utilizando Flask y SQLAlchemy, junto con una Pipeline de CI/CD con Jenkins.

## Arquitectura del Software

La aplicación web está escrita en Python con el framework Flask. Utiliza una arquitectura de microservicios, donde la lógica de negocio se separa en distintos módulos o servicios.

## Ejecución de los Tests

Para ejecutar los tests, sigue estos pasos:

1. Asegúrate de tener Python y pip instalados en tu sistema.
2. Ejecuta `pip install -r requirements-test.txt`.
3. Ejecuta `pytest`.

## Ejecución del Entorno Local para Pruebas

Para ejecutar el entorno local de desarrollo, sigue estos pasos:

1. Asegúrate de tener Docker instalado en tu sistema.
2. Coloca los archivos relacionados en la raíz de tu proyecto.
3. Ejecuta `docker-compose up --build`.

## Normas de Colaboración para el Trabajo en Equipo

- Utilizamos el modelo de ramas Git basado en Feature Branching.
- Cada nueva característica se desarrolla en una rama separada y se fusiona con la rama principal (develop) mediante Pull Requests.
- Se crea un Pull Request para revisión por pares antes de fusionar una rama de características.

## Batería de Tests

La batería de tests cubre las funcionalidades clave de la aplicación y garantiza su estabilidad y fiabilidad. Se incluyen tests unitarios que cubren al menos el 80% de las líneas de código.

## Estructura del Proyecto

El proyecto está estructurado en varios archivos y directorios, incluyendo `run.py`, `app/`, `tests/`, `manage.py`, etc.

## Funcionamiento de la Aplicación

- **Inicialización de la Aplicación:** Se crea una instancia de la aplicación Flask en base a la configuración del entorno.
- **Configuración de la Base de Datos:** La aplicación configura SQLAlchemy para interactuar con la base de datos PostgreSQL.
- **Definición de Rutas:** Se definen las rutas y las funciones controladoras en `routes.py`.
- **Modelo de Datos:** Se define el modelo de datos en `models.py`.
- **Operaciones CRUD:** Se implementan las operaciones CRUD en las funciones controladoras en `routes.py`.
- **Ejecución de la Aplicación:** La aplicación se ejecuta y se accede a las rutas definidas para realizar operaciones en los datos.

## Documentación de la Pipeline de CI con Jenkins

Este documento proporciona una explicación detallada sobre la Pipeline de Integración Continua (CI) implementada con Jenkins para el proyecto.

## Contacto

Para cualquier pregunta o problema relacionado con la Pipeline de CI, ponte en contacto con Leonor.
