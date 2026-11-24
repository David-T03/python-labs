# 🚀 Módulo 03: Desarrollo Backend con FastAPI

> **Navegación rápida:** [Sobre FastAPI](#-qué-es-fastapi) • [Estructura del Módulo](#-estructura-del-módulo) • [Índice](#-índice-de-aprendizaje) • [00. Type Hints](#00-type-hints-en-python) • [01. Configuración y Servidor](#01-entorno-instalación-y-primer-servidor) • [HTTP y Docs](#-referencia-rápida-http-y-documentación)

Bienvenido a la etapa de desarrollo **Backend** del repositorio `python-labs`. Aquí dejamos atrás los scripts de consola para empezar a construir **APIs REST** modernas, rápidas y listas para producción utilizando Python y **FastAPI**.

---

## ⚡ ¿Qué es FastAPI?

**FastAPI** es un framework web moderno y de alto rendimiento para construir APIs con Python (3.8+) basado en las anotaciones de tipo estándar del lenguaje (*Type Hints*).

* **Muy rápido:** Rendimiento comparable con **NodeJS** y **Go** (construido sobre Starlette y Pydantic).
* **Intuitivo:** Excelente soporte en editores (autocompletado inteligente en todas partes) y menos tiempo de depuración.
* **Robusto:** Validación automática de datos y generación de documentación interactiva (Swagger UI y ReDoc) sin configuración extra.

🔗 **Documentación oficial:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)

---

## 📂 Estructura del Módulo

```text
03_backend_fastapi/
├── 00_type_hints.py        # Fundamentos de tipado en Python aplicados a FastAPI
├── FastAPI/                # Carpeta principal del lado servidor (Backend)
│   ├── venv/               # Entorno virtual aislado (ignorado en Git)
│   └── main.py             # Punto de entrada de la API y primeros endpoints
└── README.md               # Esta guía de estudio y documentación
```

---

## 📑 Índice de Aprendizaje

Mapa de ruta del módulo. Conforme avancemos con nuevos conceptos, se irán añadiendo aquí y desarrollando abajo:

| # | Tema | Archivo / Carpeta |
| :-: | :--- | :--- |
| **00** | [Type Hints en Python](#00-type-hints-en-python) | [`00_type_hints.py`](./00_type_hints.py) |
| **01** | [Entorno, Instalación y Primer Servidor](#01-entorno-instalación-y-primer-servidor) | [`FastAPI/main.py`](./FastAPI/main.py) |
| **02** | [Operaciones CRUD, Parámetros y Pydantic (`BaseModel`)](#02-operaciones-crud-parámetros-y-pydantic-basemodel) | [`FastAPI/users.py`](./FastAPI/users.py) |
| **03** | *Modelos de datos con Pydantic (`BaseModel`)* | *Próximamente...* |

---

## 📖 Desarrollo del Temario

---

### 00. Type Hints en Python

Python es un lenguaje de **tipado fuerte** (no permite operaciones incompatibles entre tipos sin conversión explícita, como `"5" + 5`), pero de **tipado dinámico** (una misma variable puede cambiar de tipo de dato en tiempo de ejecución).

Sin embargo, Python permite usar **Type Hints** (anotaciones de tipo opcionales). FastAPI utiliza estas anotaciones como motor principal para validar datos automáticamente, ofrecer autocompletado en el editor y generar la documentación de la API.

#### 🆚 Diferencia de escritura (Normal vs. Type Hints)

La principal diferencia radica en agregar `: tipo` después del nombre de la variable o parámetro, y `-> tipo` antes de los dos puntos para indicar qué tipo de dato devuelve una función.

| Contexto | Escritura Normal (Sin tipar) | Con Type Hints (Recomendado) |
| :--- | :--- | :--- |
| **Variables** | `nombre = "David"` | `nombre: str = "David"` |
| **Parámetros de función** | `def saludar(nombre):` | `def saludar(nombre: str):` |
| **Retorno de función** | `def sumar(a, b): return a + b` | `def sumar(a: int, b: int) -> int: return a + b` |
| **Valor por defecto** | `def crear(activo=True):` | `def crear(activo: bool = True):` |

#### 🗂️ Catálogo de Tipos Disponibles

**1. Tipos primitivos (Básicos)**
* `int` → Números enteros (`edad: int = 25`)
* `float` → Números decimales (`precio: float = 19.99`)
* `str` → Cadenas de texto (`usuario: str = "admin"`)
* `bool` → Valores booleanos (`es_activo: bool = True`)
* `bytes` → Secuencias de bytes (`archivo: bytes = b"contenido"`)

**2. Colecciones (Estructuras de datos)**
*(En Python 3.9+ se escriben directamente en minúscula sin importar nada extra)*
* `list[tipo]` → Listas con elementos de un tipo específico (`nombres: list[str] = ["Ana", "Luis"]`)
* `dict[clave, valor]` → Diccionarios (`usuario: dict[str, int] = {"id": 1, "edad": 25}`)
* `tuple[tipo1, tipo2]` → Tuplas de longitud y tipos fijos (`coordenadas: tuple[float, float] = (9.92, -84.09)`)
* `set[tipo]` → Conjuntos de elementos únicos (`tags: set[str] = {"python", "api"}`)

**3. Tipos especiales (Muy comunes en FastAPI)**
* `tipo | None` *(o `Optional[tipo]`)* → Indica que un dato puede ser de ese tipo o `None` (`apodo: str | None = None`).
* `tipo1 | tipo2` *(o `Union[tipo1, tipo2]`)* → Permite más de un tipo de dato (`id_item: int | str = "A-10"`).
* `Any` *(requiere `from typing import Any`)* → Acepta cualquier tipo de dato cuando no es posible restringirlo.

#### 💻 Código de práctica (`00_type_hints.py`)

---

### 01. Entorno, Instalación y Primer Servidor

La carpeta **`FastAPI/`** sirve para alojar todo lo correspondiente al **lado servidor** (el backend de la aplicación).

#### 📦 1. Entorno Virtual (`venv`): ¿Para qué y por qué?
Un entorno virtual es una carpeta aislada que contiene su propio intérprete de Python y sus propias librerías instaladas, completamente independiente del sistema operativo.

* **¿Por qué usarlo?** Evita conflictos de versiones entre distintos proyectos en tu computadora (por ejemplo, si un proyecto antiguo usa una versión de librería distinta a uno nuevo) y mantiene limpio el entorno global de Python.
* **¿Para qué sirve en el repositorio?** Garantiza que cualquier persona que clone el repositorio sepa exactamente qué paquetes necesita el proyecto para correr. La carpeta `venv/` se ignora en Git (`.gitignore`) para no subir cientos de megas de dependencias a GitHub.

#### 🛠️ 2. Creación del entorno e instalación de FastAPI

Ubicados en la terminal dentro de `03_backend_fastapi/FastAPI/`:

```bash
# 1. Crear el entorno virtual
python -m venv venv

# 2. Activar el entorno virtual
# En Windows (PowerShell):
.\venv\Scripts\activate
# En Linux / Mac:
source venv/bin/activate

# 3. Instalar FastAPI con todas sus dependencias (incluye Uvicorn)
pip install "fastapi[all]"
```

> **💡 Nota para Windows (PowerShell):** Si al activar el entorno virtual aparece un error de permisos sobre ejecución de scripts (`ExecutionPolicy`), ejecuta este comando una única vez y vuelve a activar el `venv`:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

#### 🦄 3. Uvicorn: ¿Qué es, para qué sirve y cómo se instala?
FastAPI es el framework donde escribimos el código de nuestras rutas y lógica, pero necesita un **servidor web ASGI** (*Asynchronous Server Gateway Interface*) capaz de escuchar peticiones HTTP en la red y devolver las respuestas. Ese servidor es **Uvicorn**.

* **¿Cómo se instala?** Se instala automáticamente al ejecutar `pip install "fastapi[all]"` (o de forma independiente mediante `pip install "uvicorn[standard]"`).
* **¿Cómo levantar el servidor?**
  ```bash
  uvicorn main:app --reload
  ```
  * `main`: Nombre del archivo Python (`main.py`).
  * `app`: Nombre de la instancia `app = FastAPI()` creada dentro de `main.py`.
  * `--reload`: Reinicia el servidor automáticamente cada vez que guardas cambios en el código (uso exclusivo para desarrollo).

*(Si en algún momento lo ejecutas fuera de un entorno virtual activo y Windows no reconoce `uvicorn` en el `PATH`, puedes usar `python -m uvicorn main:app --reload`).*

Una vez iniciado, el servidor queda corriendo en: **`[http://127.0.0.1:8000](http://127.0.0.1:8000)`**

#### 📄 4. Primer archivo del servidor (`FastAPI/main.py`)

* **`@app.get("/ruta")`**: Decorador que indica que la función responderá a peticiones HTTP de tipo **GET** en esa ruta específica.
* **`async def`**: Define una función asíncrona, lo que permite que el servidor procese múltiples solicitudes concurrentes sin bloquearse.
* **Retorno en JSON:** FastAPI convierte automáticamente los diccionarios de Python (`dict`) en respuestas **JSON** válidas.

---

## 🧭 Referencia Rápida: HTTP y Documentación

### 🌐 Códigos de Respuesta HTTP más comunes
Cada vez que un cliente realiza una petición al servidor, este responde con un código numérico estándar que indica qué ocurrió:

| Código | Estado | Significado en nuestra API |
| :-: | :--- | :--- |
| **200** | `OK` | La petición tuvo éxito y el servidor devolvió los datos esperados (ej. al entrar a `/` o `/url`). |
| **201** | `Created` | El recurso fue creado con éxito (muy utilizado en peticiones `POST`). |
| **400** | `Bad Request` | El servidor no pudo procesar la petición por tener una sintaxis o formato inválido. |
| **401 / 403** | `Unauthorized / Forbidden` | Falta autenticación o el cliente no tiene permisos para acceder al recurso. |
| **404** | `Not Found` | La ruta o recurso solicitado no existe en el servidor (ej. entrar a `/ruta-inexistente`). |
| **422** | `Unprocessable Entity` | FastAPI lo devuelve automáticamente cuando los datos enviados no cumplen con los *Type Hints* definidos. |
| **500** | `Internal Server Error` | Ocurrió un error inesperado en el código interno del servidor. |

### 📚 Documentación Interactiva Automática
Con el servidor encendido (`uvicorn main:app --reload`), FastAPI expone dos interfaces web generadas automáticamente a partir de tu código y tus *Type Hints*:

* **`[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)` → Swagger UI**
  * **¿Qué es?** Una interfaz visual e interactiva generada con Swagger UI.
  * **¿Qué muestra?** Lista todos tus endpoints agrupados por método HTTP (`GET`, `POST`, etc.), los parámetros que reciben y el esquema de respuesta. Además, incluye el botón **"Try it out"** para probar y ejecutar peticiones reales directamente desde el navegador sin necesidad de herramientas externas como Postman o Thunder Client.

* **`[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)` → ReDoc**
  * **¿Qué es?** Una vista alternativa de documentación generada con ReDoc.
  * **¿Qué muestra?** Presenta los mismos endpoints, modelos de datos y ejemplos de respuesta en un formato de lectura más limpio, continuo y estructurado, ideal como documentación técnica formal para compartir con equipos frontend o clientes.

---


### 02. Operaciones CRUD, Parámetros y Pydantic (`BaseModel`)

**CRUD** es el acrónimo de las cuatro operaciones básicas que realiza cualquier API sobre los datos: **C**reate (Crear), **R**ead (Leer), **U**pdate (Actualizar) y **D**elete (Eliminar). En HTTP, cada operación se asocia a un método específico:

| Operación CRUD | Método HTTP | Decorador FastAPI | Propósito | Código de éxito típico |
| :--- | :---: | :--- | :--- | :---: |
| **Create** (Crear) | `POST` | `@app.post()` | Enviar datos nuevos para crear un recurso. | `201 Created` |
| **Read** (Leer) | `GET` | `@app.get()` | Obtener uno o varios recursos sin modificarlos. | `200 OK` |
| **Update** (Actualizar) | `PUT` | `@app.put()` | Actualizar un recurso existente por completo. | `200 OK` |
| **Delete** (Eliminar) | `DELETE` | `@app.delete()` | Eliminar un recurso existente. | `200 OK` o `204 No Content` |

#### 🧩 1. Modelos de datos con Pydantic (`BaseModel`)
Para recibir datos complejos en el cuerpo de la petición (*Request Body*, como un JSON al hacer `POST` o `PUT`), FastAPI utiliza **Pydantic**. Al heredar de `BaseModel` y usar *Type Hints*, FastAPI valida automáticamente que los campos existan, tengan el tipo correcto y devuelve un error `422` si algo falla.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
```

#### 🔗 2. Path Parameters vs. Query Parameters
En una petición `GET`, existen dos formas principales de enviar parámetros en la URL:

* **Path Parameters (Parámetros de ruta):** Forman parte obligatoria de la URL. Se usan para identificar un recurso específico.
  * *Ejemplo:* `http://127.0.0.1:8000/user/1`
  * *Código:* `@app.get("/user/{id}")` → `async def user(id: int):`

* **Query Parameters (Parámetros de consulta):** Van después del signo `?` en la URL en formato `clave=valor` (separados por `&`). Se usan para filtrar, paginar o parámetros opcionales.
  * *Ejemplo:* `http://127.0.0.1:8000/userquery/?id=1`
  * *Código:* `@app.get("/userquery/")` → `async def user(id: int):` *(al no estar en la ruta `{id}`, FastAPI lo interpreta automáticamente como Query Parameter)*.

---

#### 🔄 3. ¿Qué es el CRUD y cómo funciona en `FastAPI/users.py`?

**CRUD** es el acrónimo de las cuatro operaciones fundamentales para gestionar datos en cualquier aplicación o base de datos: **C**reate (Crear), **R**ead (Leer), **U**pdate (Actualizar) y **D**elete (Eliminar). En una API REST, cada una de estas acciones se ejecuta llamando a una ruta mediante su método HTTP correspondiente:

| Operación CRUD | Método HTTP | Cómo se llama en nuestra API | Qué envía el cliente |
| :--- | :---: | :--- | :--- |
| **Create** (Crear) | `POST` | `POST http://127.0.0.1:8000/user` | Un objeto JSON en el *Body* con los datos del nuevo usuario. |
| **Read** (Leer todos) | `GET` | `GET http://127.0.0.1:8000/users` | Nada (devuelve la lista completa). |
| **Read** (Leer uno) | `GET` | `GET http://127.0.0.1:8000/user/1` *(Path)*<br>`GET http://127.0.0.1:8000/userquery?id=1` *(Query)* | El `id` del usuario directamente en la URL. |
| **Update** (Actualizar) | `PUT` | `PUT http://127.0.0.1:8000/user` | Un objeto JSON en el *Body* con el `id` existente y los datos modificados. |
| **Delete** (Eliminar) | `DELETE` | `DELETE http://127.0.0.1:8000/user/1` | El `id` del usuario a eliminar en la URL. |

Para levantar este servidor independiente y probar los endpoints de usuarios, se ejecuta:
```bash
uvicorn users:app --reload
```

##### Desglose de la implementación (`users.py`):
En este archivo se simula una base de datos en memoria (`users_list`) utilizando la entidad `User` (heredada de `BaseModel` de Pydantic):

* **Read (`GET`):**
  * **`/usersjson` vs `/users`:** Compara devolver diccionarios manuales de Python frente a devolver directamente una lista de instancias `User` (que FastAPI serializa a JSON automáticamente).
  * **`/user/{id}` y `/userquery`:** Filtran `users_list` usando `filter()` y `lambda` para buscar un usuario por `id` mediante *Path* o *Query Parameters*.
* **Create (`POST` → `/user`):** Recibe un `User` en el cuerpo de la petición y verifica con la función auxiliar `search_user(user.id)` que no exista previamente antes de añadirlo con `.append()`.
* **Update (`PUT` → `/user`):** Recorre `users_list` con `enumerate()` para ubicar el índice del usuario que coincida con el `id` enviado y reemplaza el registro completo.
* **Delete (`DELETE` → `/user/{id}`):** Busca el índice del usuario por `id` y lo elimina de la lista en memoria con `del users_list[index]`.
* **Manejo de errores:** Controla casos donde el usuario no existe o ya está registrado (usando `try / except` y banderas booleanas como `found`), devolviendo mensajes JSON descriptivos (`{"error": "..."}`).

---

#### 🧪 4. ¿Dónde y cómo probar los endpoints?

Los navegadores web solo permiten hacer peticiones `GET` directamente desde la barra de direcciones. Para probar operaciones `POST`, `PUT` y `DELETE` se utilizan clientes HTTP o la documentación interactiva:

1. **Postman (o Thunder Client / Insomnia):**
   * **¿Qué es?** Una herramienta especializada para construir, enviar y guardar peticiones HTTP a APIs.
   * **¿Cómo probar el CRUD en Postman?**
     1. Selecciona el método HTTP en el desplegable (`GET`, `POST`, `PUT` o `DELETE`) y escribe la URL (ej. `http://127.0.0.1:8000/user`).
     2. Para peticiones **`POST`** y **`PUT`**, ve a la pestaña **Body** → selecciona **raw** → elige el formato **JSON** en el menú derecho y escribe el cuerpo de la petición:
        ```json
        {
          "id": 4,
          "name": "Carlos",
          "username": "Álvarez",
          "age": 24
        }
        ```
     3. Haz clic en **Send** para visualizar la respuesta JSON y el código de estado HTTP devuelto por el servidor.

2. **Swagger UI (`http://127.0.0.1:8000/docs`):**
   * Permite probar exactamente las mismas peticiones `GET`, `POST`, `PUT` y `DELETE` directamente desde el navegador usando el botón **"Try it out"**, sin instalar programas adicionales.

---