import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re

def main():
    url = "https://www.atptour.com/en/scores/current/delray-beach/499/daily-schedule"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")

    matches = []

    for match in soup.find_all(['div', 'span', 'strong'], class_=['schedule']):
        try:
            player = match.find('div', class_='player').text.strip()
            opponent = match.find('div', class_='opponent').text.strip()

            player = re.sub(r'\s+', ' ', player).strip()
            opponent = re.sub(r'\s+', ' ', opponent).strip()

            matchtime = match.find('span', class_='matchtime').text.strip()
            schedule_type = match.find('div', class_='schedule-type').text.strip()
            match_info = {'Player': player, 'Opponent': opponent, 'Matchtime': matchtime, 'Schedule Type': schedule_type}
            matches.append(match_info)
        except AttributeError:
            continue
    df = pd.DataFrame(matches)

    print(df)


if __name__ == "__main__":
    main()


# https://www.youtube.com/watch?v=Ew44dS0mw-E