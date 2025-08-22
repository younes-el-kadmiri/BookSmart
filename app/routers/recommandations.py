# app/routers/recommandations.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db_lib
from app.ml.utils import get_all_books
from app.ml.tfidf_model import build_tfidf_model, load_model
from app.ml.recommender import recommend_by_title, recommend_by_description

router = APIRouter(prefix="/recommandations", tags=["Recommandations"])

class QueryDesc(BaseModel):
    description: str
    top_n: int = 5

class QueryTitre(BaseModel):
    titre: str
    top_n: int = 5

@router.post("/build-model")
def build_model(db: Session = Depends(get_db_lib)):
    livres = get_all_books(db)
    if not livres:
        raise HTTPException(400, "Aucun livre en base.")
    build_tfidf_model(livres)
    return {"message": f"Modèle construit sur {len(livres)} livres."}

@router.post("/par-titre")
def reco_par_titre(payload: QueryTitre):
    try:
        recos = recommend_by_title(payload.titre, top_n=payload.top_n)
        if not recos:
            raise HTTPException(404, "Titre non trouvé ou pas de recommandations.")
        return {"query": payload.titre, "recommandations": recos}
    except FileNotFoundError:
        raise HTTPException(400, "Modèle non construit. Appelle /recommandations/build-model d'abord.")

@router.post("/par-description")
def reco_par_description(payload: QueryDesc):
    try:
        recos = recommend_by_description(payload.description, top_n=payload.top_n)
        return {"query": payload.description, "recommandations": recos}
    except FileNotFoundError:
        raise HTTPException(400, "Modèle non construit. Appelle /recommandations/build-model d'abord.")

@router.get("/ping-model")
def ping_model():
    try:
        _ = load_model()
        return {"ready": True}
    except FileNotFoundError:
        return {"ready": False}
