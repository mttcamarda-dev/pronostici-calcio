import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# URL base dei risultati (Champions ed Europa League)
FLASH_SCORE_URLS = {
    "Champions League": "https://www.flashscore.com/football/champions-league/",
    "Europa League": "https://www.flashscore.com/football/europa-league/"
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
