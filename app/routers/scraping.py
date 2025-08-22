# app/routers/scraping.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
import requests
from bs4 import BeautifulSoup
import re

from app.database import get_db_lib as get_db
from app.models.livre_model import Livre

router = APIRouter(prefix="/scraping", tags=["Scraping"])

# ---------- Fonction de scraping ----------
def scrape_books(base_url: str, max_pages: int = 50):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }
    books = []

    for page in range(1, max_pages + 1):
        url = f"{base_url}/catalogue/page-{page}.html"
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")

        for article in soup.select("article.product_pod"):
            title = article.h3.a["title"]
            price_raw = article.select_one(".price_color").text.strip()
            price_clean = float(re.sub(r"[^\d.]", "", price_raw))
            availability = article.select_one(".availability").text.strip()

            product_url = base_url + "/catalogue/" + article.h3.a["href"]
            prod_resp = requests.get(product_url, headers=headers, timeout=10)
            prod_soup = BeautifulSoup(prod_resp.text, "html.parser")

            # Catégorie et genre
            category = prod_soup.select("ul.breadcrumb li a")[-1].text.strip()
            genre = category

            # Description du produit
            desc_tag = prod_soup.find("div", id="product_description")
            if desc_tag:
                description = desc_tag.find_next_sibling("p").text.strip()
            else:
                description = "Aucune description"

            books.append({
                "titre": title,
                "auteur": "Inconnu",
                "prix": price_clean,
                "disponibilite": availability.lower() != "out of stock",
                "categorie": category,
                "genre": genre,
                "description": description,   # <-- ajouté
            })

    return books


# ---------- Endpoint principal ----------
@router.post("/livres")
def launch_scraping(db: Session = Depends(get_db), max_pages: int = 50):
    base_url = "https://books.toscrape.com"

    try:
        livres = scrape_books(base_url, max_pages=max_pages)

        for data in livres:
            stmt = insert(Livre).values(
                titre=data["titre"],
                auteur=data["auteur"],
                prix=data["prix"],
                disponible=data["disponibilite"],
                categorie=data["categorie"],
                genre=data["genre"],
            )

            # ⚡ Si doublon sur "titre", on met à jour les colonnes
            stmt = stmt.on_conflict_do_update(
                index_elements=['titre'],
                set_={
                    "auteur": data["auteur"],
                    "prix": data["prix"],
                    "disponible": data["disponibilite"],
                    "categorie": data["categorie"],
                    "genre": data["genre"],
                }
            )
            db.execute(stmt)

        db.commit()

        return {"message": f"{len(livres)} livres insérés ou mis à jour"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ---------- Endpoint de test ----------
@router.get("/test")
def test_scraping(db: Session = Depends(get_db)):
    """Test du scraping sur 50 pages"""
    return launch_scraping(db, max_pages=50)
