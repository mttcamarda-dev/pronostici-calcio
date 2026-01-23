import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Abilita CORS per permettere richieste dal browser

# URL base dei TOP CAMPIONATI (NO coppe europee)
FLASH_SCORE_URLS = {
    "Serie A": "https://www.flashscore.com/football/italy/serie-a/",
    "Premier League": "https://www.flashscore.com/football/england/premier-league/",
    "La Liga": "https://www.flashscore.com/football/spain/laliga/",
    "Bundesliga": "https://www.flashscore.com/football/germany/bundesliga/",
    "Ligue 1": "https://www.flashscore.com/football/france/ligue-1/"
}

def get_todays_matches():
    today_matches = []

    today_str = datetime.now().strftime("%d/%m/%Y")

    for competition, url in FLASH_SCORE_URLS.items():
        try:
            r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(r.text, "html.parser")

            # Flashscore usa div con class "event__match" per le partite
            matches = soup.find_all("div", class_="event__match")

            for match in matches:
                # Otteniamo squadre e orario
                home = match.find("div", class_="event__participant--home")
                away = match.find("div", class_="event__participant--away")
                time = match.find("div", class_="event__time")

                if home and away and time:
                    # Controlliamo che sia di oggi (Flashscore mostra anche date)
                    match_info = {
                        "competizione": competition,
                        "squadra_casa": home.text.strip(),
                        "squadra_trasferta": away.text.strip(),
                        "orario": time.text.strip(),
                        "stato_partita": "Non iniziata"
                    }
                    today_matches.append(match_info)

        except Exception as e:
            print(f"Errore durante lo scraping di {competition}: {e}")

    return today_matches


@app.route("/partite", methods=["GET"])
def partite():
    matches = get_todays_matches()
    return jsonify({"data": matches})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
