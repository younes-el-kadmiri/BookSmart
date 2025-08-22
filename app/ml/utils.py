# app/ml/utils.py
from sqlalchemy.orm import Session
from app.models.livre_model import Livre

def get_all_books(db: Session):
    """Retourne une liste de dicts pour tous les livres."""
    livres = db.query(Livre).all()
    return [
        {
            "id": l.id_livre,
            "titre": l.titre or "",
            "auteur": l.auteur or "",
            "categorie": l.categorie or "",
            "genre": l.genre or "",
            "disponible": bool(l.disponible),
            "prix": float(l.prix) if l.prix is not None else 0.0,
            # Texte pour TF-IDF : concat titre + auteur + categorie + genre
            "texte": " ".join(filter(None, [l.titre, l.auteur, l.categorie, l.genre]))
        }
        for l in livres
    ]
