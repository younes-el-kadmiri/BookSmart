# app/services/scraping_service.py
import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from app.models.livre_model import Livre

class LivreScraper:
    def __init__(self, db: Session):
        self.db = db

    def scrap_livres(self, url: str):
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": f"Impossible de récupérer les données, status {response.status_code}"}

        soup = BeautifulSoup(response.text, "html.parser")

        # Exemple : extraire titre et auteur (à adapter selon le site)
        livres_elements = soup.find_all("div", class_="livre-item")  # adapter la balise
        livres = []
        for elem in livres_elements:
            titre = elem.find("h2", class_="titre-livre").text.strip()
            auteur = elem.find("p", class_="auteur-livre").text.strip()
            # tu peux ajouter plus de champs comme année, description, etc.

            # Créer un objet Livre et l'ajouter à la DB
            livre_obj = Livre(titre=titre, auteur=auteur)
            self.db.add(livre_obj)
            livres.append(livre_obj)

        self.db.commit()
        return {"message": f"{len(livres)} livres ajoutés", "livres": [l.titre for l in livres]}
