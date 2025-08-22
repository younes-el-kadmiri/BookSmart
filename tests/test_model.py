from sqlalchemy.orm import Session
from app.database import get_db_lib as get_db  # pour la base bibliothèque
# ou
from app.database import get_db_scrap as get_db  # pour la base scraping
from app.ml.utils import get_all_books
from app.ml.tfidf_model import build_tfidf_model
from app.ml.recommender import recommend_books

db: Session = next(get_db())
livres = get_all_books(db)

# Créer le modèle
build_tfidf_model(livres)

# Tester la recommandation
recommandations = recommend_books("Sapiens: A Brief History of Humankind", top_n=5)
for r in recommandations:
    print(r["titre"], "-", r["auteur"])
