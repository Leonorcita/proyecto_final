# Proyecto DevOps

Este proyecto implementa una API RESTful utilizando Flask y SQLAlchemy, junto con una Pipeline de CI con Jenkins.

## Arquitectura del Software

La aplicación web está escrita en Python con el framework Flask. Utiliza una arquitectura de microservicios, donde la lógica de negocio se separa en distintos módulos o servicios.

## Imagen

## Prerrequisitos

1. Instalar Docker.
2. Instalar Visual Studio Code.
3. Instalar Git.
4. Ejecutar el siguiente comando para clonar repositorio `git clone https://github.com/Leonorcita/proyecto_final.git`.
5. Setear usuario de git `git config --global user.email "you@example.com"` + `git config --global user.name "Your Name"`.
6. Creación de branch propia.
7. Comenzar a modificar el código.

## Montaje del Entorno Local de Pruebas

1. Ejecutar `docker-compose up --build`.
2. Ejecuta `docker exec -it proyecto_final_web_1 /bin/bash`.
3. Para acceder a la base de datos: `psql -h proyecto_final_db_1 -U myuser -d mydatabase`.

## Ejecución de los Tests

Para ejecutar los tests, sigue estos pasos:

1. Ejecuta `make pytest`.
2. Visualización de errores en el código para su resolución.
3. Si no hay errores, realizar la actualización del código.

## Finalizar Entorno de Pruebas

1. Para salir del Entorno utilizar el comando `exit`.
2. Para destruir el Entorno al finalizar la jornada: `docker-compose down`.

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
