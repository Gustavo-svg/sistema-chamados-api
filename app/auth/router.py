from fastapi import APIRouter, HTTPException
from .schemas import UserCreate, User

router = APIRouter(prefix="/auth", tags=["Auth"])

users_db = []

@router.post("/register", response_model=User)
def register(user: UserCreate):
    for u in users_db:
        if u.email == user.email:
            raise HTTPException(
                status_code=400,
                detail="Email já cadastrado"
            )

    novo_usuario = User(
        id=len(users_db) + 1,
        email=user.email
    )

    users_db.append(novo_usuario)
    return novo_usuario

