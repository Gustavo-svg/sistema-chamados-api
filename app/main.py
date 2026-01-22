from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.chamados.router import router as chamados_router

app = FastAPI()

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)


app.include_router(chamados_router)

@app.get("/")
async def root():
    return {"message": "API Funcionando com Sucesso"}

