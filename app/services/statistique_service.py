from sqlalchemy.orm import Session
from app.models.livre_model import Livre
from app.models.emprunt_model import Emprunt

class StatistiqueService:

    def __init__(self, db: Session):
        self.db = db

    def total_livres(self):
        return self.db.query(Livre).count()

    def total_emprunts(self):
        return self.db.query(Emprunt).count()

    def emprunts_par_livre(self):
        return self.db.query(Emprunt.livre_id, func.count(Emprunt.id)).group_by(Emprunt.livre_id).all()
