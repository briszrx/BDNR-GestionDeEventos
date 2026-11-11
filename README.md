# BDNR-GestionDeEventos

## Integrantes
| Nombre | Expediente |
|--------|------------|
| Allison Avila | 757985 |
| Isaac Garcia | 739528 |
| Carlos Maldonado | 750849 |
 
## Descripción
Plataforma de gestión de eventos y registro de actividad de usuarios. Controla
disponibilidad, categorías y cambios de los eventos, y lleva un seguimiento
auditable de asistencias, tiempos de estadía e interacciones (aportaciones,
incidentes, agresiones). Permite a los administradores analizar la participación
histórica, cuidar la seguridad de las sedes y evaluar el rendimiento por
categoría y sede.
 
Cada base de datos resuelve una parte distinta:
- **Cassandra:** historial, bitácoras y métricas por usuario, sede y categoría.
- **MongoDB:** catálogo de eventos (detalles, agenda, boletaje, búsqueda de texto).
- **Dgraph:** red social entre usuarios y eventos (recomendaciones, co-asistencia).

## Estructura de Proyecto 
```
project-name/
├── Cassandra/  - definiciones de Cassandra
├── Mongo/      - definiciones de MongoDB
├── Dgraph/     - definiciones de Dgraph
├── data/       - datos de prueba (Faker / CSV / JSON)
├── connect.py  - conexiones a las 3 bases de datos
├── populate.py - plan para poblar las bases de datos
├── main.py     - menú de consultas
└── README.md   - Instrucciones para 
```
## Flujo de trabajo (borrador)
 
### 1. Levantar los contenedores
```bash
docker run -d --name eventos-cassandra -p 9042:9042 cassandra:latest
docker run -d --name eventos-mongo -p 27017:27017 mongo:latest
docker run -d --name eventos-dgraph -p 8080:8080 -p 9080:9080 dgraph/standalone:latest
```
 
### 2. Crear el ambiente virtual
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1      # Windows (PowerShell)
source venv/bin/activate         # Linux / Mac
```
 
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
 
### 4. Ejecutar
1. Probar conexiones: `python connect.py`
2. Poblar las bases de datos con datos de prueba: `python populate.py`
3. Ejecutar el menú de consultas: `python main.py`