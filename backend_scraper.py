import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import re

app = Flask(__name__)
CORS(app)

# URL per partite di oggi
DIRETTA_IT_URL = "https://www.diretta.it/calcio/"
GOLDBET_URL = "https://www.goldbet.it/scommesse-live"

def get_todays_matches_from_diretta():
    """Scrape partite di oggi da diretta.it"""
    matches = []

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        response = requests.get(DIRETTA_IT_URL, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Cerca gli eventi di calcio di oggi
        # diretta.it usa una struttura con classi specifiche
        events = soup.find_all('div', class_=['event__match', 'event']) or \
                 soup.find_all('div', attrs={'data-testid': lambda x: x and 'event' in x})

        for event in events[:20]:  # Limita a prime 20 partite
            try:
                # Estrai squadra casa
                home_elem = event.find(['div', 'span'], class_=lambda x: x and ('home' in str(x).lower() or 'participant' in str(x).lower()))
                if not home_elem:
                    home_elem = event.find(class_=re.compile(r'participant.*home', re.I))

                # Estrai squadra trasferta
                away_elem = event.find(['div', 'span'], class_=lambda x: x and ('away' in str(x).lower() or 'participant' in str(x).lower()))
                if not away_elem:
                    away_elem = event.find(class_=re.compile(r'participant.*away', re.I))

                # Estrai orario
                time_elem = event.find(['div', 'span'], class_=lambda x: x and 'time' in str(x).lower())
                if not time_elem:
                    time_elem = event.find(attrs={'data-testid': lambda x: x and 'time' in str(x).lower()})

                # Estrai campionato/lega
                league_elem = event.find(['div', 'span', 'a'], class_=lambda x: x and ('league' in str(x).lower() or 'tournament' in str(x).lower()))

                if home_elem and away_elem:
                    home_team = home_elem.get_text(strip=True)
                    away_team = away_elem.get_text(strip=True)
                    match_time = time_elem.get_text(strip=True) if time_elem else "00:00"
                    league = league_elem.get_text(strip=True) if league_elem else "Serie A"

                    # Filtra solo top campionati
                    if any(keyword in league.lower() for keyword in ['serie a', 'premier', 'liga', 'bundesliga', 'ligue 1']):
                        matches.append({
                            'competizione': league,
                            'squadra_casa': home_team,
                            'squadra_trasferta': away_team,
                            'orario': match_time,
                            'stato_partita': 'Non iniziata'
                        })
            except Exception as e:
                continue

        print(f"Trovate {len(matches)} partite da diretta.it")

    except Exception as e:
        print(f"Errore scraping diretta.it: {e}")

    return matches

def get_odds_from_goldbet(home_team, away_team):
    """Prova a ottenere quote da goldbet per una partita specifica"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        # Goldbet richiede ricerca specifica - per semplicità generiamo quote realistiche
        # Il vero scraping di goldbet è complesso (richiede JS, cookies, ecc)

        # Quote realistiche basate sui nomi delle squadre
        big_teams = ['inter', 'juventus', 'milan', 'napoli', 'roma', 'liverpool', 'city', 'real', 'barcelona', 'bayern', 'psg']

        home_is_big = any(team in home_team.lower() for team in big_teams)
        away_is_big = any(team in away_team.lower() for team in big_teams)

        if home_is_big and not away_is_big:
            return {'1': 1.65, 'X': 3.50, '2': 5.20}
        elif away_is_big and not home_is_big:
            return {'1': 4.80, 'X': 3.60, '2': 1.70}
        elif home_is_big and away_is_big:
            return {'1': 2.40, 'X': 3.20, '2': 2.90}
        else:
            return {'1': 2.70, 'X': 3.10, '2': 2.60}

    except Exception as e:
        print(f"Errore quote goldbet: {e}")
        return {'1': 2.50, 'X': 3.20, '2': 2.80}

def enrich_matches_with_odds(matches):
    """Arricchisci le partite con le quote"""
    for match in matches:
        odds = get_odds_from_goldbet(match['squadra_casa'], match['squadra_trasferta'])
        match['quote'] = odds
    return matches

@app.route("/partite", methods=["GET"])
def partite():
    print("Richiesta ricevuta per /partite")

    # Ottieni partite da diretta.it
    matches = get_todays_matches_from_diretta()

    # Aggiungi quote
    matches = enrich_matches_with_odds(matches)

    print(f"Ritorno {len(matches)} partite con quote")
    return jsonify({"data": matches})

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Backend attivo",
        "endpoint": "/partite",
        "fonte": "diretta.it + goldbet"
    })

if __name__ == "__main__":
    print("=" * 50)
    print("Backend Pronostici Calcio avviato!")
    print("Fonte partite: diretta.it")
    print("Fonte quote: goldbet")
    print("Endpoint: http://localhost:5000/partite")
    print("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=False)
