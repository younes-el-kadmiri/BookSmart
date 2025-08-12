mkdir -p booksmart/{app/{models,routers,services,ml,scraping,schemas,utils},templates/admin,static/{css,js,img},data/recommandations,tests}

touch booksmart/app/__init__.py
touch booksmart/app/main.py
touch booksmart/app/database.py

# Models
touch booksmart/app/models/{__init__.py,adherent.py,livre.py,emprunt.py,reservation.py,historique.py,notification.py}

# Routers
touch booksmart/app/routers/{__init__.py,auth.py,adherents.py,livres.py,emprunts.py,reservations.py,recommandations.py,statistiques.py}

# Services
touch booksmart/app/services/{__init__.py,auth_service.py,livre_service.py,recommandation_service.py,scraping_service.py,statistique_service.py}

# ML
touch booksmart/app/ml/{__init__.py,tfidf_model.py,similarity.py}
touch booksmart/app/ml/model.pkl  # (vide pour l'instant)

# Scraping
touch booksmart/app/scraping/{__init__.py,scrap_books_toscrape.py}

# Schemas
touch booksmart/app/schemas/{__init__.py,auth.py,livre.py,emprunt.py,reservation.py,historique.py,notification.py}

# Utils
touch booksmart/app/utils/{__init__.py,security.py,email_service.py,config.py}

# Templates
touch booksmart/templates/{base.html,home.html,inscription.html,login.html,livre.html,profil.html,recommandation-par-description.html}
touch booksmart/templates/admin/{gestion-adherents.html,gestion-livres.html,emprunts.html,statistiques.html}

# Static files
touch booksmart/static/css/style.css
touch booksmart/static/js/main.js

# Data
touch booksmart/data/{livres_bruts.csv,livres_nettoyes.csv}
touch booksmart/data/recommandations/similarity_matrix.pkl

# Tests
touch booksmart/tests/{__init__.py,test_auth.py}

# Root files
touch booksmart/{requirements.txt,.env,README.md,run.sh}
