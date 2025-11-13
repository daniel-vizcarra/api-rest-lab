# Guía de Evidencias para el Informe

Esta guía describe todas las capturas de pantalla que necesitas tomar para completar el informe del taller.

## Estado Actual del Proyecto

✅ **API REST implementada completamente con FastAPI**
✅ **Servidor corriendo en http://localhost:8000**
✅ **Todos los archivos creados y subidos a GitHub**

---

## Evidencias Requeridas por Sección

### 📸 Sección 2.1 - Preparación del Entorno

#### Evidencia 1: Creación y activación del entorno virtual
**Qué hacer:**
1. Abre una terminal nueva
2. Navega al directorio del proyecto: `cd api-rest-lab`
3. Ejecuta: `python3 -m venv venv`
4. Ejecuta: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
5. Toma captura mostrando el prompt con `(venv)` al inicio

**Qué debe verse:** Terminal mostrando los comandos ejecutados y el prompt con (venv)

#### Evidencia 2: Instalación de dependencias
**Qué hacer:**
1. Con el entorno virtual activado, ejecuta: `pip install fastapi uvicorn`
2. Toma captura mostrando las dependencias instalándose
3. Ejecuta: `pip list | grep -E "fastapi|uvicorn|pydantic"`
4. Toma captura mostrando las versiones instaladas

**Qué debe verse:** Proceso de instalación y lista de paquetes instalados

---

### 📸 Sección 2.2 - Estructura del Proyecto

#### Evidencia 3: Estructura de archivos
**Qué hacer:**
1. Ejecuta en terminal: `ls -la`
2. O abre el explorador de archivos mostrando la carpeta del proyecto
3. O abre VS Code mostrando el árbol de archivos en el panel lateral

**Qué debe verse:**
- main.py
- requirements.txt
- README.md
- openapi.json
- postman_collection.json
- .gitignore
- venv/

---

### 📸 Sección 2.3 - Modelo de Dominio

#### Evidencia 4: Código del modelo Envio
**Qué hacer:**
1. Abre `main.py` en un editor de código
2. Muestra las líneas que contienen:
   - La clase `Envio(BaseModel)`
   - La lista `envios_db`
3. Toma captura mostrando ambas partes del código

**Qué debe verse:** Definición de la clase Envio con sus campos (id, destinatario, direccion, estado) y la lista envios_db con datos de ejemplo

---

### 📸 Sección 2.4 - Implementación de Endpoints REST

#### Evidencia 5: Código de los endpoints
**Qué hacer:**
1. Abre `main.py`
2. Toma capturas mostrando cada decorador y función:
   - `@app.get("/envios")`
   - `@app.get("/envios/{id}")`
   - `@app.post("/envios")`

**Qué debe verse:** Código completo de cada endpoint con sus decoradores, parámetros y lógica

#### Evidencia 6: Pruebas en Swagger
**Qué hacer:**
1. Asegúrate que el servidor esté corriendo: `uvicorn main:app --reload`
2. Abre en navegador: http://127.0.0.1:8000/docs
3. Toma captura de la página principal de Swagger
4. Para cada endpoint, haz clic en "Try it out" y "Execute":
   - GET /envios
   - GET /envios/1
   - POST /envios (usa el JSON de ejemplo)
   - GET /health
5. Toma captura de cada respuesta exitosa

**Qué debe verse:** Interfaz de Swagger con las respuestas en formato JSON

---

### 📸 Sección 2.5 - Endpoint de Salud

#### Evidencia 7: Respuesta del /health
**Qué hacer:**
1. En Swagger, ejecuta GET /health
2. O ejecuta en terminal: `curl http://localhost:8000/health`
3. Toma captura mostrando la respuesta: `{"status": "ok"}`

**Qué debe verse:** Respuesta JSON con status "ok"

---

### 📸 Sección 2.6 - Documentación Swagger/OpenAPI

#### Evidencia 8: Página /docs con lista de endpoints
**Qué hacer:**
1. Abre: http://127.0.0.1:8000/docs
2. Toma captura mostrando TODOS los endpoints listados
3. Asegúrate que se vean los métodos (GET/POST) y las rutas

**Qué debe verse:** Interfaz completa de Swagger UI con todos los endpoints expandibles

#### Evidencia 9: Pruebas desde Swagger
**Qué hacer:**
Ya las hiciste en la evidencia 6, usa esas mismas capturas

#### Evidencia 10: Contrato OpenAPI en JSON
**Qué hacer:**
1. Abre en navegador: http://127.0.0.1:8000/openapi.json
2. Toma captura mostrando el JSON formateado
3. O abre el archivo `openapi.json` en un editor y toma captura

**Qué debe verse:** Estructura JSON del contrato OpenAPI 3.0

---

### 📸 Sección 2.7 - Ejecución Reproducible

#### Evidencia 11: Servidor corriendo
**Qué hacer:**
1. Ejecuta: `uvicorn main:app --reload`
2. Espera a que aparezcan los logs:
   ```
   INFO:     Uvicorn running on http://127.0.0.1:8000
   INFO:     Application startup complete.
   ```
3. Haz algunas peticiones con curl o desde el navegador
4. Toma captura mostrando los logs con las peticiones registradas

**Qué debe verse:**
- Terminal con el servidor corriendo
- Logs de inicio
- Logs de peticiones HTTP con códigos de estado (200, 201, 404, etc.)

---

### 📸 Sección 2.8 - Pruebas con Postman

#### Evidencia 12: Respuestas en Postman
**Qué hacer:**
1. Abre Postman
2. Importa el archivo `postman_collection.json`
3. Asegúrate que el servidor esté corriendo
4. Ejecuta cada petición y toma capturas:
   - GET http://localhost:8000/health
   - GET http://localhost:8000/envios
   - GET http://localhost:8000/envios/1
   - POST http://localhost:8000/envios (con body JSON)
5. Muestra la respuesta de cada petición

**Qué debe verse:**
- Panel de Postman con la petición configurada
- Respuesta JSON en el panel inferior
- Código de estado (200, 201, etc.)

#### Evidencia 13: Exportación de colección
**Qué hacer:**
1. En Postman, haz clic derecho en la colección
2. Selecciona "Export"
3. Toma captura del diálogo de exportación
4. O muestra el archivo `postman_collection.json` en el explorador

**Qué debe verse:** Proceso de exportación o archivo JSON en el sistema

---

## 📋 Capturas Adicionales Recomendadas

### Git y GitHub
**Qué hacer:**
1. Ejecuta: `git log --oneline -5`
2. Toma captura mostrando los commits
3. Abre GitHub en el navegador
4. Muestra el repositorio con los archivos subidos

**Qué debe verse:** Historial de commits y repositorio en GitHub

### Estructura del código
**Qué hacer:**
1. Toma captura panorámica del archivo `main.py` completo
2. Resalta las secciones principales con comentarios

---

## ✅ Checklist de Evidencias

Marca cada evidencia conforme la tomes:

- [ ] 1. Creación y activación del entorno virtual
- [ ] 2. Instalación de dependencias
- [ ] 3. Estructura de archivos del proyecto
- [ ] 4. Código del modelo Envio y envios_db
- [ ] 5. Código de los endpoints REST
- [ ] 6. Pruebas en Swagger de cada endpoint
- [ ] 7. Respuesta del endpoint /health
- [ ] 8. Página /docs con lista de endpoints
- [ ] 9. Pruebas interactivas desde Swagger
- [ ] 10. Contrato OpenAPI JSON
- [ ] 11. Servidor corriendo con logs de peticiones
- [ ] 12. Respuestas en Postman (4 capturas mínimo)
- [ ] 13. Exportación de colección de Postman

---

## 📝 Notas Importantes

1. **Calidad de capturas:**
   - Usa buena resolución
   - Asegúrate que el texto sea legible
   - Muestra información relevante completa

2. **Nombres de archivos:**
   - Usa nombres descriptivos como:
     - `evidencia_01_entorno_virtual.png`
     - `evidencia_06_swagger_get_envios.png`
     - `evidencia_12_postman_health.png`

3. **Servidor debe estar corriendo:**
   - Para las capturas de Swagger y Postman, el servidor debe estar ejecutándose
   - Ejecuta: `uvicorn main:app --reload`

4. **Organización:**
   - Guarda todas las capturas en la carpeta `evidencias/`
   - Numera las capturas según el orden del informe

---

## 🚀 Comandos Rápidos de Referencia

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Ejecutar servidor
uvicorn main:app --reload

# Probar endpoints con curl
curl http://localhost:8000/health
curl http://localhost:8000/envios
curl http://localhost:8000/envios/1
curl -X POST http://localhost:8000/envios -H "Content-Type: application/json" -d '{"id":5,"destinatario":"Test","direccion":"Test","estado":"Pendiente"}'

# Ver estructura del proyecto
ls -la

# Ver commits
git log --oneline -5
```

---

## 📧 Información del Proyecto

**Estudiantes:** Sammy Porras, Daniel Vizcarra
**Curso:** Integración de Sistemas
**Universidad:** Universidad de Las Américas
**Fecha:** 14/11/2025

---

**¡Éxito con las evidencias!** 🎉
