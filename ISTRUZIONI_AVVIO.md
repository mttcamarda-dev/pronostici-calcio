# 🚀 Come Avviare Pronostici Calcio

## ⚽ Partite REALI dei TOP 5 Campionati Europei

Questa applicazione mostra le partite **REALI di oggi** da:
- 🇮🇹 **Serie A** (Italia)
- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 **Premier League** (Inghilterra)
- 🇪🇸 **La Liga** (Spagna)
- 🇩🇪 **Bundesliga** (Germania)
- 🇫🇷 **Ligue 1** (Francia)

**Nessuna coppa europea** (Champions, Europa, Conference) - Solo campionati nazionali.

---

## 📋 Requisiti

- **Python 3.7+** installato
- **Browser web** (Chrome, Firefox, Safari, Edge)

---

## 🎯 Avvio Rapido (2 Passi)

### 1. Installa Dipendenze (Solo la Prima Volta)

Apri un terminale nella cartella del progetto ed esegui:

```bash
pip install -r requirements.txt
```

Questo installerà:
- Flask (server web)
- BeautifulSoup4 (scraping HTML)
- requests (richieste HTTP)
- flask-cors (gestione CORS)

---

### 2. Avvia il Backend

Nel terminale, esegui:

```bash
python backend_scraper.py
```

Vedrai:
```
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

✅ **Il backend è attivo!**

---

### 3. Apri l'Applicazione

**Apri `index.html` nel browser** (doppio click o trascina nel browser).

Vedrai le partite REALI di oggi dei 5 top campionati europei!

---

## ⚙️ Come Funziona

1. **Backend Python** (`backend_scraper.py`):
   - Fa scraping di FlashScore.com
   - Estrae partite di oggi dai 5 campionati
   - Espone API REST su `http://localhost:5000/partite`

2. **Frontend** (`index.html`):
   - Chiama l'API del backend
   - Mostra partite con design moderno
   - Calcola pronostici basati su statistiche
   - Aggiorna automaticamente ogni 2 minuti

---

## 🔄 Workflow Giornaliero

**Ogni volta che vuoi vedere le partite:**

1. Apri terminale
2. `python backend_scraper.py`
3. Apri `index.html` nel browser
4. Lascia il terminale aperto mentre usi l'app

**Per fermare il backend:**
- Premi `Ctrl+C` nel terminale

---

## ❓ FAQ

### Vedo "Backend locale non attivo"

Il backend Python non è in esecuzione. Esegui `python backend_scraper.py`.

### Vedo 0 partite

Possibili cause:
1. Non ci sono partite oggi in quei campionati (normale nei giorni infrasettimanali)
2. FlashScore ha cambiato la struttura HTML (richiede aggiornamento codice)
3. Problema di connessione a FlashScore

### Posso vedere anche le coppe europee?

Il backend è configurato per **escludere** le coppe. Se vuoi includerle, modifica `backend_scraper.py` aggiungendo gli URL delle coppe.

### Voglio dati da un'API ufficiale

Puoi cambiare fonte dati in `index.html`:

**API-Football** (tutte le competizioni):
1. Vai su [RapidAPI](https://rapidapi.com/api-sports/api/api-football)
2. Crea account → Piano FREE
3. Copia chiave API
4. In `index.html`: `DATA_SOURCE: 'rapidapi'` e `API_KEY: 'TUA_CHIAVE'`

---

## ⚠️ Note Legali

- Questo tool fa **web scraping** di FlashScore
- Usalo **solo per scopo personale/educativo**
- Non condividere pubblicamente o usare commercialmente
- Il web scraping potrebbe violare i ToS di FlashScore
- Per uso professionale, usa API ufficiali (API-Football, Football-Data.org)

---

## 🎨 Personalizzazione

### Aggiungere altri campionati

Modifica `backend_scraper.py`:

```python
FLASH_SCORE_URLS = {
    "Serie A": "https://www.flashscore.com/football/italy/serie-a/",
    "Premier League": "https://www.flashscore.com/football/england/premier-league/",
    # Aggiungi qui:
    "Eredivisie": "https://www.flashscore.com/football/netherlands/eredivisie/",
}
```

### Cambiare colori

Modifica `index.html` nella sezione `<style>` (cerca i codici colore come `#667eea`).

---

## 📞 Supporto

- Problemi con il backend: Controlla i log nel terminale
- Problemi con il frontend: Apri Console del browser (F12)
- Nessuna partita: Normale se oggi non ci sono match in quei campionati

---

## ✅ Checklist Avvio

- [ ] Python installato (`python --version`)
- [ ] Dipendenze installate (`pip install -r requirements.txt`)
- [ ] Backend avviato (`python backend_scraper.py`)
- [ ] Terminale aperto e in esecuzione
- [ ] `index.html` aperto nel browser
- [ ] Vedi partite (o messaggio "nessuna partita oggi")

---

**Buon divertimento! ⚽🎉**
