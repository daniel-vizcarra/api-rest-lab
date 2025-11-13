# API de Gestión de Envíos - Taller de Integración de Sistemas

## Descripción

API REST desarrollada con **Python + FastAPI** para la gestión de envíos, cumpliendo con los principios RESTful y las mejores prácticas de integración de sistemas.

## Stack Tecnológico

- **Python 3.11+**
- **FastAPI 0.121.1** - Framework web moderno y de alto rendimiento
- **Uvicorn 0.38.0** - Servidor ASGI de alto rendimiento
- **Pydantic 2.12.4** - Validación de datos y serialización

## Características

✅ Implementación completa de endpoints REST (GET, POST)
✅ Generación automática de documentación OpenAPI 3.0
✅ Documentación interactiva con Swagger UI
✅ Validación automática de datos con Pydantic
✅ Endpoint de salud `/health` para monitoreo
✅ Respuestas en formato JSON
✅ Manejo de errores HTTP apropiado

## Endpoints Disponibles

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Información básica de la API |
| GET | `/health` | Verificación de salud del servicio |
| GET | `/envios` | Obtener todos los envíos |
| GET | `/envios/{id}` | Obtener un envío por ID |
| POST | `/envios` | Crear un nuevo envío |

## Instalación y Configuración

### Prerrequisitos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**

```bash
git clone <url-del-repositorio>
cd api-rest-lab
```

2. **Crear y activar el entorno virtual**

**En Linux/MacOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Instalar las dependencias**

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el servidor de desarrollo:

```bash
uvicorn main:app --reload
```

El servidor se ejecutará en: `http://127.0.0.1:8000`

**Parámetros del comando:**
- `main:app` - Módulo y aplicación de FastAPI
- `--reload` - Recarga automática ante cambios en el código (solo desarrollo)

## Documentación

Una vez ejecutado el servidor, puedes acceder a:

- **Swagger UI (Documentación interactiva):** http://127.0.0.1:8000/docs
- **ReDoc (Documentación alternativa):** http://127.0.0.1:8000/redoc
- **Contrato OpenAPI 3.0 (JSON):** http://127.0.0.1:8000/openapi.json

## Uso de la API

### Ejemplos con cURL

**1. Verificar salud del servicio:**
```bash
curl http://127.0.0.1:8000/health
```

**2. Obtener todos los envíos:**
```bash
curl http://127.0.0.1:8000/envios
```

**3. Obtener un envío específico:**
```bash
curl http://127.0.0.1:8000/envios/1
```

**4. Crear un nuevo envío:**
```bash
curl -X POST http://127.0.0.1:8000/envios \
  -H "Content-Type: application/json" \
  -d '{
    "id": 4,
    "destinatario": "Pedro Sánchez",
    "direccion": "Av. Naciones Unidas 500, Quito",
    "estado": "Pendiente"
  }'
```

## Estructura del Proyecto

```
api-rest-lab/
├── venv/                          # Entorno virtual de Python
├── main.py                        # Código principal de la API
├── requirements.txt               # Dependencias del proyecto
├── README.md                      # Este archivo
├── openapi.json                   # Contrato OpenAPI 3.0 (generado)
├── postman_collection.json        # Colección de Postman
└── Taller APIREST.pdf            # Documentación del taller
```

## Modelo de Datos

### Envio

```json
{
  "id": 1,
  "destinatario": "Juan Pérez",
  "direccion": "Av. República 123, Quito",
  "estado": "En tránsito"
}
```

**Campos:**
- `id` (int): Identificador único del envío
- `destinatario` (str): Nombre del destinatario
- `direccion` (str): Dirección de entrega
- `estado` (str): Estado del envío (Pendiente, En tránsito, Entregado)

## Códigos de Estado HTTP

- `200 OK` - Solicitud exitosa
- `201 Created` - Recurso creado exitosamente
- `400 Bad Request` - Error en los datos enviados
- `404 Not Found` - Recurso no encontrado
- `500 Internal Server Error` - Error interno del servidor

## Pruebas

### Con Swagger UI

1. Accede a http://127.0.0.1:8000/docs
2. Explora los endpoints disponibles
3. Haz clic en "Try it out" para probar cada endpoint
4. Completa los parámetros requeridos
5. Haz clic en "Execute" para enviar la petición

### Con Postman

1. Importa el archivo `postman_collection.json`
2. Asegúrate de que el servidor esté corriendo
3. Ejecuta las peticiones de la colección

## Integrantes

- **Sammy Porras**
- **Daniel Vizcarra**

## Curso

**Integración de Sistemas**
Universidad de Las Américas
Facultad de Ingenierías y Ciencias Agropecuarias
Ingeniería De Software

## Fecha

14/11/2025

## Licencia

Este proyecto es parte de un taller académico de la Universidad de Las Américas.
