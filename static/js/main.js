// static/js/main.js

const API = {
  livres: "/livres",
  search: (q) => `/livres/search/?q=${encodeURIComponent(q)}`,
  reservations: "/reservations",
  recoBuild: "/recommandations/build-model",
  recoTitre: "/recommandations/par-titre",
  recoDesc: "/recommandations/par-description",
};

async function fetchJSON(url, opts={}){
  const r = await fetch(url, {headers:{'Content-Type':'application/json'}, ...opts});
  if(!r.ok){ throw new Error(await r.text()); }
  return r.json();
}

async function searchBooks() {
  const query = document.getElementById('search').value;
  const category = document.getElementById('category').value;
  const genre = document.getElementById('genre').value;
  const grid = document.getElementById('books-grid');

  try {
    const res = await fetch(`/livres/search/?q=${encodeURIComponent(query)}&category=${encodeURIComponent(category)}&genre=${encodeURIComponent(genre)}`);
    if (!res.ok) {
      grid.innerHTML = `<p>Erreur: ${res.status} ${res.statusText}</p>`;
      return;
    }
    const data = await res.json();

    grid.innerHTML = '';
    if (!Array.isArray(data) || data.length === 0) {
      grid.innerHTML = '<p>Aucun livre trouvé.</p>';
      return;
    }

    data.forEach(book => {
      const div = document.createElement('div');
      div.className = 'book-card';
      div.innerHTML = `
        <h3>${book.titre}</h3>
        <p>${book.auteur}</p>
        <p>Catégorie: ${book.categorie}</p>
        <p>Genre: ${book.genre}</p>
        <p>Prix: ${book.prix} MAD</p>
      `;
      grid.appendChild(div);
    });
  } catch (err) {
    grid.innerHTML = `<p>Erreur lors de la récupération des livres: ${err}</p>`;
  }
}


function cardBook(b){
  const dispo = b.disponible ? '<span class="badge ok">Disponible</span>' : '<span class="badge no">Indisponible</span>';
  const price = b.prix != null ? `<div class="price">€ ${Number(b.prix).toFixed(2)}</div>` : '';
  return `
  <div class="card">
    <h3>${escapeHTML(b.titre)}</h3>
    <div class="muted">${escapeHTML(b.auteur || 'Auteur inconnu')}</div>
    <div class="row" style="justify-content:space-between; align-items:center; margin:.6rem 0">${dispo}${price}</div>
    <div class="row">
      <a class="btn ghost" href="/livre.html?id=${b.id_livre || b.id}">Détails</a>
      ${b.disponible ? `<button class="btn primary" onclick="reserve(${b.id_livre || b.id})">Réserver</button>` : ''}
    </div>
  </div>`;
}

function escapeHTML(s){ return (s||'').replace(/[&<>"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m])); }

async function reserve(id_livre, id_adherent=1){
  try{
    const payload = { id_livre, id_adherent, date_reservation: new Date().toISOString().slice(0,10) };
    await fetchJSON(API.reservations, {method:'POST', body:JSON.stringify(payload)});
    alert("Réservation enregistrée ✅");
  }catch(e){ alert("Erreur réservation: " + e.message); }
}

async function buildReco(){
  try{
    const r = await fetchJSON(API.recoBuild, {method:'POST'});
    alert(r.message || "Modèle reconstruit");
  }catch(e){ alert("Erreur build modèle: "+ e.message); }
}

async function recoByTitle(inputId='titre', gridId='reco-grid'){
  const titre = document.getElementById(inputId).value.trim();
  if(!titre){ alert("Donne un titre"); return; }
  const res = await fetchJSON(API.recoTitre, {method:'POST', body: JSON.stringify({titre, top_n:5})});
  renderReco(res.recommandations, gridId);
}

async function recoByDesc(inputId='desc', gridId='reco-grid'){
  const description = document.getElementById(inputId).value.trim();
  if(!description){ alert("Écris une description"); return; }
  const res = await fetchJSON(API.recoDesc, {method:'POST', body: JSON.stringify({description, top_n:5})});
  renderReco(res.recommandations, gridId);
}

function renderReco(items, gridId='reco-grid'){
  const grid = document.getElementById(gridId);
  if(!items || !items.length){ grid.innerHTML = '<p class="muted">Aucune reco.</p>'; return; }
  grid.innerHTML = items.map(cardBook).join('');
}
