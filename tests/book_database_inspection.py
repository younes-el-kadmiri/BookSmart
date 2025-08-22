# app/routers/display_lib.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db_lib
from app.models import Livre, Utilisateur, Emprunt

router = APIRouter(prefix="/display_lib", tags=["display_lib"])

@router.get("/livres")
def get_livres(db: Session = Depends(get_db_lib)):
    return db.query(Livre).all()

@router.get("/utilisateurs")
def get_utilisateurs(db: Session = Depends(get_db_lib)):
    return db.query(Utilisateur).all()

@router.get("/emprunts")
def get_emprunts(db: Session = Depends(get_db_lib)):
    return db.query(Emprunt).all()
