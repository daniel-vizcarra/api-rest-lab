from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

# Crear instancia de FastAPI
app = FastAPI(
    title="API de Gestión de Envíos",
    description="API REST para gestionar envíos - Taller de Integración de Sistemas",
    version="1.0.0"
)

# Modelo de dominio: Envio
class Envio(BaseModel):
    id: int
    destinatario: str
    direccion: str
    estado: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "destinatario": "Juan Pérez",
                "direccion": "Av. República 123, Quito",
                "estado": "En tránsito"
            }
        }

# Base de datos en memoria (simula una BD real)
envios_db: List[Envio] = [
    Envio(id=1, destinatario="María García", direccion="Calle 10 de Agosto 456, Quito", estado="Entregado"),
    Envio(id=2, destinatario="Carlos López", direccion="Av. Amazonas 789, Quito", estado="En tránsito"),
    Envio(id=3, destinatario="Ana Rodríguez", direccion="Calle Colón 321, Quito", estado="Pendiente")
]

# Endpoint raíz
@app.get("/", tags=["Root"])
def root():
    """
    Endpoint raíz que proporciona información básica de la API
    """
    return {
        "mensaje": "API de Gestión de Envíos",
        "version": "1.0.0",
        "documentacion": "/docs"
    }

# Endpoint de salud
@app.get("/health", tags=["Health"])
def health_check():
    """
    Endpoint de salud para verificar que el servicio está funcionando correctamente.
    Útil para monitoreo y despliegues automatizados.
    """
    return {"status": "ok"}

# GET /envios - Obtener todos los envíos
@app.get("/envios", response_model=List[Envio], tags=["Envíos"])
def obtener_envios():
    """
    Retorna la lista completa de envíos almacenados en el sistema
    """
    return envios_db

# GET /envios/{id} - Obtener un envío por ID
@app.get("/envios/{id}", response_model=Envio, tags=["Envíos"])
def obtener_envio_por_id(id: int):
    """
    Retorna un envío específico basado en su ID

    - **id**: Identificador único del envío
    """
    # Buscar el envío en la base de datos
    for envio in envios_db:
        if envio.id == id:
            return envio

    # Si no se encuentra, retornar error 404
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Envío con ID {id} no encontrado"
    )

# POST /envios - Crear un nuevo envío
@app.post("/envios", response_model=Envio, status_code=status.HTTP_201_CREATED, tags=["Envíos"])
def crear_envio(envio: Envio):
    """
    Crea un nuevo envío en el sistema

    - **id**: Identificador único del envío
    - **destinatario**: Nombre del destinatario
    - **direccion**: Dirección de entrega
    - **estado**: Estado actual del envío (Pendiente, En tránsito, Entregado)
    """
    # Verificar si ya existe un envío con ese ID
    for env in envios_db:
        if env.id == envio.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ya existe un envío con ID {envio.id}"
            )

    # Agregar el envío a la base de datos
    envios_db.append(envio)

    return envio
