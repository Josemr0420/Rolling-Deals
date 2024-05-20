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

### Servicio API

El proyecto incluye un servicio API para obtener información. La ruta para acceder a la API es:

```
http://127.0.0.1:8000/api/hotwheels/
```

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Mira el archivo [LICENSE](LICENSE) para más detalles.
```

Este README incluye ahora la información sobre el servicio API en tu aplicación. Si necesitas más detalles o alguna otra modificación, házmelo saber.
