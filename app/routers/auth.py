from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db_lib
from app.models import Utilisateur
from passlib.context import CryptContext
from app.services.auth_service import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Login(BaseModel):
    email: str
    mot_de_passe: str

@router.post("/token")
def login(login: Login, db: Session = Depends(get_db_lib)):
    user = db.query(Utilisateur).filter(Utilisateur.email == login.email).first()
    if not user or not pwd_context.verify(login.mot_de_passe, user.mot_de_passe):
        raise HTTPException(status_code=400, detail="Email ou mot de passe incorrect")
    access_token = create_access_token({"user_id": user.id_utilisateur, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}
