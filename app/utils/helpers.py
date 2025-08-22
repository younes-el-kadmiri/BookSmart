from datetime import datetime

def format_datetime(dt: datetime) -> str:
    """Formate un datetime en string lisible."""
    return dt.strftime("%d/%m/%Y %H:%M:%S")

def slugify(text: str) -> str:
    """Transforme un texte en slug URL-friendly."""
    return text.lower().replace(" ", "-")
