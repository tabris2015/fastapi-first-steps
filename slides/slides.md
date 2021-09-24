---
marp: true
theme: gaia
class: invert
---
# Tu primera REST API con Python y FastAPI
#### Meetup 01: Python para todos
Jose Laruta

![bg right 100%](img/logo-fastapi.png)

Python La Paz - Septiembre, 2021

---
# Agenda
  1. El protocolo HTTP en la web
  2. REST
  3. APIs REST
  4. FastAPI 
  5. Demo

---
## HTTP - Hypertext Transfer Protocol

Protocolo sobre la capa de **aplicación** base de la comunicaciòn en la web.

Los documentos de **hipertexto** incluyen **hipervínculos** a otros recursos y son simples de acceder.

---
## HTTP - Hypertext Transfer Protocol

HTTP está basado en el flujo **petición-respuesta** o *request-response* sobre un modelo cliente-servidor.

 - El cliente envía una petición o *request* al servidor :rocket:. 
 - El servidor responde con un recurso (ej: archivo HTML) :truck:

La respuesta o *response* posee información del resultado de la petición y otro contenido en el *body*

---
## REST - Representational state transfer
---
## API - Application Programming Interface