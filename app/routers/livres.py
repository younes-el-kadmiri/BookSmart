from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.livre import LivreCreate, LivreSchema
from app.services.livre_service import LivreService
from app.database import get_db_lib
from fastapi import Query

router = APIRouter(prefix="/livres", tags=["Livres"])

router = APIRouter()
@router.get("/", response_model=List[LivreSchema])
def get_all_livres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_lib)):
    service = LivreService(db)
    livres = service.get_livres(skip=skip, limit=limit)
    return livres

@router.get("/{livre_id}", response_model=LivreSchema)
def get_livre(livre_id: int, db: Session = Depends(get_db_lib)):
    service = LivreService(db)
    livre = service.get_livre_by_id(livre_id)
    if not livre:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    return livre

@router.post("/", response_model=LivreSchema)
def create_livre(livre: LivreCreate, db: Session = Depends(get_db_lib)):
    service = LivreService(db)
    return service.create_livre(livre)


from fastapi import Query

@router.get("/livres/search", response_model=List[LivreSchema])
def search_livres(
    db: Session = Depends(get_db_lib),
    q: str = Query("", description="Recherche par titre ou auteur"),
    category: str = Query(None),
    skip: int = 0,
    limit: int = 10,
):
    query = db.query(Livre)
    if q:
        query = query.filter(Livre.titre.ilike(f"%{q}%") | Livre.auteur.ilike(f"%{q}%"))
    if category:
        query = query.filter(Livre.categorie == category)
    return query.offset(skip).limit(limit).all()




