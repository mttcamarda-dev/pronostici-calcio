# Backend FlashScore Scraper - Quick Start

## ⚠️ Importante

**Questo backend scraping FlashScore è fornito solo per scopo educativo.**

- ⚠️ Il web scraping potrebbe violare i Terms of Service di FlashScore
- ⚠️ Potresti essere bannato se fai troppe richieste
- ⚠️ Il codice si romperà se FlashScore cambia la struttura HTML
- ✅ Per uso in produzione, usa l'API-Football (opzione consigliata)

---

## Setup Rapido

### 1. Installa le dipendenze

```bash
cd /home/user/pronostici-calcio
pip install -r requirements.txt
```

Questo installerà:
- Flask (web framework)
- requests (HTTP client)
- beautifulsoup4 (HTML parser)

### 2. Avvia il backend

```bash
python backend_scraper.py
```

Output:
```
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

### 3. Testa l'endpoint

In un altro terminale:

```bash
curl http://localhost:5000/partite
```

Risposta esempio:
```json
{
  "data": [
    {
      "competizione": "Champions League",
      "squadra_casa": "Real Madrid",
      "squadra_trasferta": "Liverpool",
      "orario": "21:00",
      "stato_partita": "Non iniziata"
    }
  ]
}
```

### 4. Configura il frontend

Apri `index.html` e trova la configurazione (circa riga 471):

```javascript
const API_CONFIG = {
    DATA_SOURCE: 'local', // ← CAMBIA IN 'local'
    // ...
};
```

### 5. Apri index.html nel browser

Dovresti vedere le partite di Champions League ed Europa League.

---

## Come Funziona

1. **Flask Backend**: Server HTTP su porta 5000
2. **Web Scraping**: Usa `requests` e `BeautifulSoup` per analizzare HTML di FlashScore
3. **Endpoint `/partite`**: Restituisce JSON con le partite
4. **Frontend**: `index.html` fa richiesta HTTP a `localhost:5000` e mostra i dati

---

## Risoluzione Problemi

### Errore CORS

Se vedi errori CORS nel browser:

```bash
pip install flask-cors
```

Aggiungi in `backend_scraper.py`:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ← Aggiungi questa riga
```

### Backend non raggiungibile

- Assicurati che il backend sia in esecuzione (`python backend_scraper.py`)
- Verifica che non ci siano altri servizi sulla porta 5000
- Controlla i log del backend per errori

### Nessuna partita trovata

- FlashScore potrebbe aver cambiato la struttura HTML
- Controlla i log del backend: `Errore durante lo scraping...`
- Ispeziona la pagina FlashScore con DevTools per vedere le classi CSS aggiornate

### Selettori CSS non funzionano

Se FlashScore cambia la struttura, aggiorna i selettori in `backend_scraper.py`:

```python
# Trova i nuovi class names su FlashScore
matches = soup.find_all("div", class_="NUOVO_CLASS_NAME")
home = match.find("div", class_="NUOVO_CLASS_HOME")
away = match.find("div", class_="NUOVO_CLASS_AWAY")
```

---

## Limitazioni

| Feature | Backend Locale | API-Football |
|---------|---------------|--------------|
| Champions League | ✅ | ✅ |
| Europa League | ✅ | ✅ |
| Conference League | ❌ | ✅ |
| Serie A | ❌ | ✅ |
| Premier League | ❌ | ✅ |
| La Liga | ❌ | ✅ |
| Bundesliga | ❌ | ✅ |
| Ligue 1 | ❌ | ✅ |
| API Key richiesta | ❌ | ✅ |
| Affidabilità | ⚠️ Fragile | ✅ Stabile |
| Legalità | ⚠️ ToS risk | ✅ Legale |

---

## Aggiungere Altre Competizioni

Per aggiungere Conference League o altre coppe:

1. Trova l'URL FlashScore della competizione
2. Aggiungi in `FLASH_SCORE_URLS`:

```python
FLASH_SCORE_URLS = {
    "Champions League": "https://www.flashscore.com/football/champions-league/",
    "Europa League": "https://www.flashscore.com/football/europa-league/",
    "Conference League": "https://www.flashscore.com/football/conference-league/",
    "Serie A": "https://www.flashscore.com/football/italy/serie-a/",
}
```

---

## Conclusione

**Per uso personale e apprendimento:**
- ✅ Usa questo backend per sperimentare con web scraping
- ✅ Ottimo per capire Flask, requests, BeautifulSoup

**Per uso reale/produzione:**
- ❌ NON usare questo backend (fragile, potenzialmente illegale)
- ✅ Usa API-Football con RapidAPI (più stabile, legale, completo)

---

**Domande?** Leggi `BACKEND_INTEGRATION.md` per dettagli completi.
