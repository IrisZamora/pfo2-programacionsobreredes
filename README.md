# PFO 2: Sistema de Gestión de Tareas con API y Base de Datos

Github page: [https://iriszamora.github.io/pfo2-programacionsobreredes/](https://iriszamora.github.io/pfo2-programacionsobreredes/)

## Instrucciones para ejecutar el proyecto

1. Clonar el repositorio:

git clone [https://github.com/IrisZamora/pfo2-programacionsobreredes.git](https://github.com/IrisZamora/pfo2-programacionsobreredes.git)

cd pfo2-programacionsobreredes

2. Crear entorno virtual:

python -m venv venv

3. Activar entorno:

venv\Scripts\activate

4. Instalar dependencias: 

pip install flask flask-bcrypt flask-sqlalchemy

5. Ejecutar API: 

python servidor.py

El servidor se ejecutará en: http://127.0.0.1:5000

6.Cliente por consola para interactuar con la API

- Instalar dependecia:

pip install requests

-Ejecutar: 

Primero tener corriendo el servidor y en otra terminal ejecutá: python cliente.py

Aparecerá un menú, ingresá la opción que desees y seguí las instrucciones por consola.


### Endpoints y pruebas

Endpoints disponibles:

- POST /registro: Registra un nuevo usuario.

- POST /login: Inicia sesión.

- GET /tareas: Página de bienvenida a tareas.


- Pruebas con Postman:

✅POST: http://127.0.0.1:5000/registro

Registro exitoso:

![Registro exitoso](capturas/postman/registroExitoso.png)

Intento de registrar usuario existente:

![Registro usuario existente](capturas/postman/usuarioExiste.png)

✅POST: http://127.0.0.1:5000/login

Login Exitoso:

![Login Exitoso](capturas/postman/loginExitoso.png)

Login fallido:

![Login fallido](capturas/postman/credencialesIncorrectas.png)

✅GET: http://127.0.0.1:5000/tareas

Página de tareas:

![Tareas bienvenida](capturas/postman/pantallaTareas.png)

- Pruebas utilizando Cliente por consola:

Registro exitoso:

![Registro exitoso](capturas/clienteConsola/registroExitoso.png)

Intento de registrar usuario existente:

![Registro usuario existente](capturas/clienteConsola/usuarioExiste.png)

Login Exitoso:

![Login Exitoso](capturas/clienteConsola/login.png)

Login fallido:

![Login fallido](capturas/clienteConsola/credencialesIncorrectas.png)

Página de tareas:

![Tareas bienvenida](capturas/clienteConsola/verTareas.png)

#### Respuestas conceptuales

- ¿Por qué hashear contraseñas?

Porque guardar contraseñas en texto plano es un riesgo de seguridad. Si alguien accede a la base de datos, las podría ver. Hashearlas significa que se guarda una versión encriptada que no se puede revertir fácilmente.

- Ventajas de usar SQLite en este:

SQLite es una base de datos ligera, sin necesidad de servidor, ideal para proyectos chicos. Facilita pruebas y despliegue rápido sin configuraciones complejas. Además es fácil de integrar con Flask.











