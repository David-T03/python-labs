from fastapi import FastAPI

app = FastAPI()

# Se define una ruta raíz que devuelve un mensaje de saludo
@app.get("/")
async def root():
    return "Hello World"

# Se define una ruta "/url" que devuelve un diccionario con una URL específica
@app.get("/url")
async def url():
    return {"url": "https://www.youtube.com/watch?v=iHVfWvKDuac&pp=ygUMbm9uIHNlcnZpdW0g"}