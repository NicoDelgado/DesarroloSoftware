from fastapi import FastAPI

app = FastAPI()

@app.get("/Bienvenido")
async def root():
    return{"message": "Bienvenidos, a FastDelivery"}

@app.get("/usuarios/{user_id}")
async def read_user(user_id: int):
        return{"user_id": user_id}

paquetes = [{"paquete": "Memoria RAM 8 GB"}, {"paquete": "Silla Ergonomica Negra"}, {"paquete": "Mouse Inalambrico"}, {"paquete": "Disco Duro SSD 250 gb"}]

@app.get("/paquetes/")
async def read_item(skip: int = 0, limit: int = 10):
    return paquetes[skip : skip + limit]