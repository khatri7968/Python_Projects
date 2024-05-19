import requests
from bs4 import BeautifulSoup
import pandas as pd

LIMIT_PAGES = True


def scrape_players():
    url = "https://www.transfermarkt.co.uk/spieler-statistik/wertvollstespieler/marktwertetop?land_id=0&ausrichtung=alle&spielerposition_id=alle&altersklasse=alle&jahrgang=0&kontinent_id=0&plus=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    players = []

    table = soup.find('table', class_='items')
    rows = table.find_all('tr', class_=['odd', 'even'])

    for row in rows:
        player_data = {}

        # Get player name
        name = row.find('a', class_='spielprofil_tooltip')
        player_data['Name'] = name.text

        # Get player details
        details = row.find_all('td', class_='zentriert')
        player_data['Age'] = details[0].text
        player_data['Citizenship'] = details[1].img['title']
        player_data['Position'] = details[2].text
        player_data['Current Club'] = details[3].img['alt']

        # Get player statistics
        stats = row.find_all('td', class_='rechts')
        player_data['Appearances'] = stats[0].text
        player_data['Goals'] = stats[1].text
        player_data['Assists'] = stats[2].text
        player_data['Yellow Cards'] = stats[3].text
        player_data['Second Yellows'] = stats[4].text
        player_data['Red Cards'] = stats[5].text
        player_data['Starting Eleven'] = stats[6].text
        player_data['Minutes'] = stats[7].text
        player_data['Goal Participation'] = stats[8].text

        # Get player market value
        market_value = row.find('td', class_='rechts mw')
        player_data['Current Market Value'] = market_value.text.strip()

        players.append(player_data)

    return players


def export_to_excel(players):
    df = pd.DataFrame(players)
    df.to_excel('players.xlsx', index=False)


def main():
    players = scrape_players()
    export_to_excel(players)
    print("Data scraped and exported to 'players.xlsx'.")


if __name__ == '__main__':
    main()
