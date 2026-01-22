# Backend Integration Guide - FlashScore Scraper

## Overview

You now have **TWO options** for fetching football match data:

1. **API-Football (RapidAPI)** - Current implementation in `index.html`
   - ✅ Official API, reliable, structured data
   - ✅ 100+ competitions worldwide
   - ⚠️ Requires free API key (100 requests/day)

2. **FlashScore Scraper Backend** - New Python backend in `backend_scraper.py`
   - ✅ No API key needed
   - ✅ Champions League & Europa League only
   - ⚠️ Requires running Python server
   - ⚠️ Web scraping may violate FlashScore ToS
   - ⚠️ Breaks if FlashScore changes HTML structure

---

## Option 1: Use Current API-Football (Recommended)

**Already integrated in `index.html`**

### Pros:
- Official API with legal access
- Reliable, stable data structure
- All competitions worldwide (Serie A, Premier League, Champions League, etc.)
- No server infrastructure needed
- Mobile-friendly, works anywhere

### Setup:
1. Get free API key: https://rapidapi.com/api-sports/api/api-football
2. Edit `index.html` line 476: `API_KEY: 'your-key-here'`
3. Open `index.html` in browser

---

## Option 2: Use FlashScore Scraper Backend

**New backend that scrapes FlashScore website**

### Architecture:
```
┌─────────────────┐         ┌──────────────────┐         ┌──────────────────┐
│  index.html     │  HTTP   │  Flask Backend   │  HTTP   │  FlashScore.com  │
│  (Frontend)     │────────▶│  backend_scraper │────────▶│  (Website)       │
│  JavaScript     │◀────────│  (Python)        │◀────────│                  │
└─────────────────┘  JSON   └──────────────────┘  HTML   └──────────────────┘
```

### Pros:
- No API key required
- Free, unlimited requests
- Direct data from FlashScore

### Cons:
- **Legal concerns**: Web scraping may violate Terms of Service
- **Fragile**: Breaks if FlashScore changes their HTML
- **Limited**: Only Champions League & Europa League
- **Infrastructure**: Requires Python server running locally
- **CORS issues**: Need to configure cross-origin requests

### Installation:

#### Step 1: Install Python dependencies
```bash
cd /home/user/pronostici-calcio
pip install -r requirements.txt
```

#### Step 2: Run the Flask backend
```bash
python backend_scraper.py
```

Server will start on `http://localhost:5000`

#### Step 3: Test the backend
```bash
curl http://localhost:5000/partite
```

Expected response:
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

#### Step 4: Update frontend to use local backend

Replace the API configuration in `index.html` (around line 472):

**Original (API-Football):**
```javascript
const API_CONFIG = {
    API_KEY: '',
    API_HOST: 'api-football-v1.p.rapidapi.com',
    API_BASE_URL: 'https://api-football-v1.p.rapidapi.com/v3',
    TIMEOUT: 15000
};
```

**New (FlashScore Scraper):**
```javascript
const API_CONFIG = {
    USE_LOCAL_BACKEND: true,
    LOCAL_BACKEND_URL: 'http://localhost:5000',
    TIMEOUT: 15000
};
```

#### Step 5: Update fetch function

Replace `fetchTodayMatches()` function (around line 526) with:

```javascript
async function fetchTodayMatches() {
    if (API_CONFIG.USE_LOCAL_BACKEND) {
        // Use local Flask backend
        const url = `${API_CONFIG.LOCAL_BACKEND_URL}/partite`;

        const response = await fetchWithTimeout(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Backend error: ${response.status}`);
        }

        const data = await response.json();

        // Transform to expected format
        return data.data.map(match => ({
            fixture: {
                id: Math.random(),
                date: new Date().toISOString(),
                status: {
                    short: 'NS',
                    long: 'Not Started'
                }
            },
            league: {
                name: match.competizione,
                country: 'Europe',
                logo: '',
                flag: '🇪🇺'
            },
            teams: {
                home: {
                    name: match.squadra_casa,
                    logo: ''
                },
                away: {
                    name: match.squadra_trasferta,
                    logo: ''
                }
            },
            goals: {
                home: null,
                away: null
            },
            score: {
                halftime: { home: null, away: null },
                fulltime: { home: null, away: null }
            }
        }));
    } else {
        // Original API-Football logic
        // ... (keep existing code)
    }
}
```

---

## Important Considerations

### Legal & Ethical Issues

⚠️ **Web Scraping Warning:**
- FlashScore's Terms of Service may prohibit automated scraping
- Could result in IP bans or legal action
- Not recommended for production/commercial use
- Use only for educational purposes with caution

### Technical Issues

**CORS (Cross-Origin Resource Sharing):**
If you get CORS errors, add to `backend_scraper.py`:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
```

Install CORS support:
```bash
pip install flask-cors
```

**FlashScore HTML Changes:**
FlashScore frequently updates their website structure. If scraping stops working:
1. Inspect FlashScore's HTML in browser DevTools
2. Update CSS selectors in `get_todays_matches()`
3. Look for new class names like `event__match`, `event__participant--home`, etc.

---

## Recommendation

**For personal use: Use API-Football (Option 1)**
- More reliable and legal
- Better data coverage (all leagues)
- No server infrastructure needed
- Free tier sufficient for personal use

**For experimentation only: Use FlashScore Scraper (Option 2)**
- Educational purposes only
- Understand web scraping techniques
- No API key dependency
- Not recommended for production

---

## Hybrid Approach

You can implement **fallback logic**:

```javascript
async function fetchTodayMatches() {
    try {
        // Try API-Football first
        if (API_CONFIG.API_KEY) {
            return await fetchFromAPIFootball();
        }
    } catch (error) {
        console.warn('API-Football failed, trying local backend:', error);
    }

    try {
        // Fallback to local scraper
        return await fetchFromLocalBackend();
    } catch (error) {
        console.error('All sources failed:', error);
        throw error;
    }
}
```

---

## Current Status

- ✅ API-Football integration: **Already implemented in index.html**
- ✅ FlashScore scraper backend: **Saved as backend_scraper.py**
- ⏳ Frontend integration: **Requires manual update to index.html**

Let me know which approach you prefer and I can update the frontend accordingly.
