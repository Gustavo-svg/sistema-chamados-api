from fastapi import APIRouter, HTTPException
from .schemas import UserCreate, User, UserLogin

router = APIRouter()

users_db = []

@router.post("/register", response_model=User)
def register(user: UserCreate):
    for u in users_db:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo_usuario = {
        "id": len(users_db) + 1,
        "email": user.email,
        "password": hash_password(user.password)
    }

    users_db.append(novo_usuario)
    return {"id": novo_usuario["id"], 
            "email": novo_usuario["email"]

    }

   


@router.post("/login")
def login(user: UserLogin):
    for u in users_db:
        if u.email == user.email:
            return {"acess_token": token,
                    "token_type" : "bearer"            
            }

    raise HTTPException(status_code=401, detail="Credenciais inválidas")

