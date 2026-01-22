from pydantic import BaseModel

class ChamadoCreate(BaseModel):
    titulo: str
    descricao: str

class Chamado(BaseModel):
    id: int
    titulo: str
    descricao: str
