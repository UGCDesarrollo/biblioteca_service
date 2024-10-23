# Servicio de Biblioteca

Este servicio desarrollado en Django permite consultar los préstamos activos de una persona en la base de datos del sistema bibliotecario Koha. A través de este servicio, se puede obtener información sobre los libros prestados, incluyendo el título, autor, fechas de préstamo y devolución.

## Características:
- Consulta de préstamos activos por documento de identificación.
- Filtros de búsqueda por título, autor y biblioteca.
- Protección mediante API Key y autenticación de usuario.

## Modelo de Datos

### `UserAPIKey`
Relaciona las llaves API con los usuarios autenticados.

### `Prestamo`
El modelo de los préstamos contiene la siguiente estructura:

- **nro_documento**: Identificación de la persona.
- **titulo**: Título del libro prestado.
- **autor**: Autor del libro.
- **biblioteca_material**: Biblioteca de donde proviene el material prestado.
- **fecha_prestamo**: Fecha en que se realizó el préstamo.
- **fecha_devolucion**: Fecha límite para devolver el libro.

El modelo está vinculado a la tabla `temporal_etl` en la base de datos.

## URLs

Las rutas disponibles en el servicio son las siguientes:

- `/prestamos/`: Lista los préstamos activos en la base de datos. Permite buscar por número de documento o por campos como título, autor, y biblioteca.

La configuración de las rutas utiliza `DefaultRouter` de Django REST Framework para registrar las vistas de los préstamos.

## Vistas

El `PrestamoViewSet` maneja las siguientes funcionalidades:

- **Queryset**: Devuelve todos los préstamos activos en la base de datos.
- **Permisos**: Requiere autenticación por API Key o usuario autenticado.
- **Filtros**: 
  - Por número de documento (`nro_documento`).
  - Búsqueda por título, autor y biblioteca.
- **Métodos permitidos**: GET para listar los préstamos.

Los filtros permiten a los usuarios realizar búsquedas más específicas, por ejemplo, consultar todos los préstamos de una persona o buscar por libro o autor.

## Configuración

A continuación, se describen las configuraciones principales del servicio:

- **Base de Datos**: El servicio utiliza PostgreSQL como sistema de base de datos, configurado mediante las siguientes variables de entorno:
  - `DB_NAME`: Nombre de la base de datos.
  - `DB_USER`: Usuario de la base de datos.
  - `DB_PASS`: Contraseña del usuario.
  - `DB_HOST`: Host de la base de datos.
  - `DB_PORT`: Puerto de conexión a la base de datos (por defecto 5432).

- **Seguridad**: 
  - El servicio está protegido mediante API Keys y autenticación de usuarios.
  - La aplicación implementa seguridad con HTTPS, cookies seguras y políticas HSTS.
  - Configuración para prevenir ataques XSS y clickjacking.

### Ejemplo de configuración:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_base_datos',
        'USER': 'usuario_base_datos',
        'PASSWORD': 'contraseña_base_datos',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


### 6. **Uso del Servicio**
Explica cómo interactuar con el servicio.

```markdown
## Uso del Servicio

### Obtener los préstamos de una persona
- **Ruta**: `/prestamos/`
- **Método**: `GET`
- **Parámetros opcionales**:
  - `nro_documento`: Filtrar préstamos por número de documento de la persona.
  - `search`: Buscar por título, autor o biblioteca.

#### Ejemplo de solicitud:
```bash
curl -H "Authorization: Api-Key TU_API_KEY" http://localhost:8000/prestamos/?nro_documento=12345678


### 7. **Iniciar el Proyecto**
Instrucciones para correr el proyecto en un entorno local.

```markdown
## Iniciar el Proyecto

### Clonar el repositorio

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio

python3 -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
pip install -r requirements.txt

DEBUG=True
SECRET_KEY=tu_clave_secreta
DB_NAME=nombre_base_datos
DB_USER=usuario_base_datos
DB_PASS=contraseña_base_datos
DB_HOST=localhost
DB_PORT=5432
CORS_ALLOWED_ORIGINS=http://localhost:8000


### 8. **Consideraciones de Seguridad**
Describe cómo asegurar la API en producción.

```markdown
## Consideraciones de Seguridad

- Utiliza HTTPS en producción.
- Configura correctamente los encabezados de seguridad (XSS, HSTS, etc.).
- No expongas las claves API o las credenciales de la base de datos en el código fuente público.
- Limita las solicitudes por IP para evitar abusos en el servicio (ej. usar ratelimit).




