# Rolling Deals

Este proyecto es una aplicación desarrollada en Django.

## Instalación y ejecución

### Prerrequisitos

Asegúrate de tener instalados los siguientes programas:

- Python 3.8
- Git
- Virtualenv

### Clonar el repositorio

```bash
git clone https://github.com/Josemr0420/Rolling-Deals.git
cd Rolling-Deals
```

### Instalación en Linux

1. **Crear y activar un entorno virtual:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

2. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Aplicar migraciones:**

   ```bash
   python manage.py migrate
   ```

4. **Crear un superusuario (opcional pero recomendado):**

   ```bash
   python manage.py createsuperuser
   ```

5. **Ejecutar el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

### Instalación en Windows

1. **Crear y activar un entorno virtual:**

   ```bash
   python -m venv env
   .\env\Scripts\activate
   ```

2. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Aplicar migraciones:**

   ```bash
   python manage.py migrate
   ```

4. **Crear un superusuario (opcional pero recomendado):**

   ```bash
   python manage.py createsuperuser
   ```

5. **Ejecutar el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

## Uso

Accede a la aplicación en tu navegador web en `http://127.0.0.1:8000/`.

## API

### Descripción General

La API de Subastas de Hot Wheels permite a los usuarios recuperar información sobre los autos de Hot Wheels y sus subastas asociadas. Este documento proporciona detalles sobre cómo interactuar con la API, incluidos los puntos finales disponibles y los formatos de respuesta.

### URL Base

La URL base para acceder a la API es:
```
http://localhost:8000/api/
```

### Endpoints

#### Obtener Lista de Hot Wheels con Subastas

- **URL:** `/api/hotwheels/`
- **Método:** `GET`
- **Descripción:** Recupera una lista de todos los autos de Hot Wheels junto con la información de sus subastas asociadas.
- **Formato de Respuesta:** JSON

##### Ejemplo de Solicitud

```http
GET http://localhost:8000/api/hotwheels/
```

##### Ejemplo de Respuesta

```json
[
    {
        "id": 10,
        "image": "http://localhost:8000/media/hotwheels/Twin_Mill.webp",
        "auction": [
            {
                "start_time": "2024-05-20T20:07:28.635300Z",
                "end_time": "2024-05-27T20:07:28.635300Z",
                "status": "upcoming",
                "starting_bid": "10.00",
                "user": 1
            }
        ],
        "model_name": "Twin Mill",
        "year_released": 1969,
        "color": "Red"
    },
    {
        "id": 11,
        "image": "http://localhost:8000/media/hotwheels/Bone_Shaker.webp",
        "auction": [
            {
                "start_time": "2024-05-20T20:07:28.641297Z",
                "end_time": "2024-05-27T20:07:28.641297Z",
                "status": "upcoming",
                "starting_bid": "10.00",
                "user": 1
            }
        ],
        "model_name": "Bone Shaker",
        "year_released": 2006,
        "color": "Black"
    },
    ...
]
```

### Esquema

#### Hotwheel

El modelo `Hotwheel` representa un auto de Hot Wheels. Incluye los siguientes campos:

- **id**: (Entero) Identificador único para el Hot Wheel.
- **model_name**: (Cadena) El nombre del modelo de Hot Wheel.
- **year_released**: (Entero) El año en que se lanzó el Hot Wheel.
- **color**: (Cadena) El color del Hot Wheel.
- **image**: (URL) La URL de la imagen del Hot Wheel.
- **auction**: (Lista) Una lista de subastas asociadas con el Hot Wheel.

#### Auction

El modelo `Auction` representa una subasta para un Hot Wheel. Incluye los siguientes campos:

- **start_time**: (Fecha y Hora) La hora de inicio de la subasta.
- **end_time**: (Fecha y Hora) La hora de finalización de la subasta.
- **status**: (Cadena) El estado de la subasta. Los valores posibles son `active`, `completed`, `upcoming`.
- **starting_bid**: (Decimal) La oferta inicial para la subasta.
- **user**: (Entero) El ID del usuario que creó la subasta.

### Cómo Usar la API

1. **Enviar una solicitud GET** a `/api/hotwheels/` para recuperar la lista de Hot Wheels y los detalles de sus subastas.
2. **Examinar la respuesta** para obtener los detalles de cada Hot Wheel y sus subastas asociadas.

### Notas

- La API actualmente solo admite el método `GET` para recuperar información.
- Las URL de las imágenes proporcionadas en la respuesta se pueden usar para mostrar imágenes de los Hot Wheels.
    
## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Mira el archivo [LICENSE](LICENSE) para más detalles.
```

Este README incluye ahora la información sobre el servicio API en tu aplicación. Si necesitas más detalles o alguna otra modificación, házmelo saber.
