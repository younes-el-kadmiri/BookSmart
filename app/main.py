from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.auth import admin_required, adherent_required  # tes dépendances JWT
from fastapi import FastAPI
from app.routers import livres  # ou ton fichier routes
from app.routers import scraping


app = FastAPI(
    title="BookSmart API",
    description="API pour la recommandation et la gestion de livres",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(livres.router)
app.include_router(scraping.router)

# Pages publiques
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/inscription")
def inscription(request: Request):
    return templates.TemplateResponse("inscription.html", {"request": request})

@app.get("/profil")
def inscription(request: Request):
    return templates.TemplateResponse("profil.html", {"request": request})

@app.get("/recommandation-par-description")
def recommandation(request: Request):
    return templates.TemplateResponse("recommandation-par-description.html", {"request": request})

# Pages sécurisées
@app.get("/dashboard")
def dashboard(request: Request, user=Depends(adherent_required)):
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})

@app.get("/admin")
def admin_dashboard(request: Request, user=Depends(admin_required)):
    return templates.TemplateResponse("admin.html", {"request": request, "user": user})
