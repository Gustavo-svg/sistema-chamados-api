from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Api Funcionando com Sucesso"}
