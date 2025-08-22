from sqlalchemy.orm import Session
from app.models.livre_model import Livre
from app.schemas.livre import LivreCreate

class LivreService:
    def __init__(self, db: Session):
        self.db = db

    def create_livre(self, livre: LivreCreate):
        db_livre = Livre(**livre.dict())
        self.db.add(db_livre)
        self.db.commit()
        self.db.refresh(db_livre)
        return db_livre

    def get_livres(self, skip: int = 0, limit: int = 10, category: str = None, genre: str = None):
        query = self.db.query(Livre)
        if category:
            query = query.filter(Livre.categorie == category)
        if genre:
            query = query.filter(Livre.genre == genre)
        return query.offset(skip).limit(limit).all()

    def get_livre_by_id(self, livre_id: int):
        return self.db.query(Livre).filter(Livre.id_livre == livre_id).first()


    