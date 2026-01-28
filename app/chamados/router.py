from fastapi import APIRouter , Depends
from app.auth.dependencies import get_current_user
from .schemas import ChamadoCreate, Chamado
from typing import List

router = APIRouter(
    prefix="/chamados", 
    tags=["Chamados"]
)

chamados_db = []

@router.get("/" , response_model=List[Chamado])
def listar_chamados(user=Depends(get_current_user)):
    return chamados_db

@router.post("/" , response_model=Chamado)
def criar_chamado(chamado: ChamadoCreate , user=Depends(get_current_user)):
    novo_chamado = Chamado(
        id=len(chamados_db) + 1,
        titulo=chamado.titulo,
        descricao=chamado.descricao
       )
    chamados_db.append(novo_chamado)
    return novo_chamado



