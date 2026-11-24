from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Para iniciar el servidor: uvicorn users:app --reload

# Entidad de usuario
class User(BaseModel):
    id: int
    name: str
    username: str
    age: int
# Lista de usuarios
users_list = [User(id=1, name="David", username="Marín", age=30),
              User(id=2, name="Juan", username="García", age=25),
              User(id=3, name="María", username="Pérez", age=28)]

# Endpoint para obtener la lista de usuarios en formato JSON
@app.get("/usersjson")
async def read_users():
    return [{"name": "David", "username": "Marín", "age": 30},
            {"name": "Juan", "username": "García", "age": 25},
            {"name": "María", "username": "Pérez", "age": 28}]

# Endpoint para obtener la lista de usuarios en formato JSON utilizando la clase User
@app.get("/users")
async def read_users_class():
    return users_list

# Endpoint con path parameter para obtener un usuario por su ID con manejo de errores
@app.get("/user/{id}")
async def read_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

# Endpoint con query parameters para obtener un usuario por su id con manejo de errores
@app.get("/userquery")
async def read_user_query(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

# Endpoint para crear un nuevo usuario con manejo de errores si el usuario ya existe
@app.post("/user")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return user

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

# Endpoint para actualizar un usuario existente con manejo de errores si el usuario no existe
@app.put("/user")
async def update_user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user

# Endpoint para eliminar un usuario existente con manejo de errores si el usuario no existe
@app.delete("/user/{id}")
async def delete_user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}
    else:
        return {"message": "Usuario eliminado correctamente"}
