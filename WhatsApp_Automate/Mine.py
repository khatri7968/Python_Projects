from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set the URL of the website to scrape
url = "https://www.transfermarkt.co.uk/spieler-statistik/wertvollstespieler/marktwertetop?land_id=0&ausrichtung=alle&spielerposition_id=alle&altersklasse=alle&jahrgang=0&kontinent_id=0&plus=1"

# Set up Chrome options
chrome_options = Options()

# Set up the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL
driver.get(url)

# Get the page source
page_source = driver.page_source

# Create a BeautifulSoup object to parse the page source
soup = BeautifulSoup(page_source, "html.parser")

# Find all the player rows in the table
player_rows = soup.select("table.items > tbody > tr.odd, table.items > tbody > tr.even")

# Iterate over each player row
for row in player_rows:
    # Extract the necessary information from each row
    name_element = row.select_one("a.spielprofil_tooltip")
    name = name_element.text if name_element else "N/A"

    age_element = row.select_one("td.zentriert.alter-transfermarkt")
    age = age_element.text if age_element else "N/A"

    citizenship_element = row.select_one("td.zentriert.nat-transfermarkt img")
    citizenship = citizenship_element["title"] if citizenship_element else "N/A"

    position_element = row.select_one("td.pos-transfermarkt")
    position = position_element.text if position_element else "N/A"

    club_elements = row.select("td.hauptlink")
    club = club_elements[1].text if len(club_elements) >= 2 else "N/A"

    # Print the extracted information
    print("Name:", name)
    print("Age:", age)
    print("Citizenship:", citizenship)
    print("Position:", position)
    print("Current Club:", club)
    print("------------------------------------")

# Quit the browser
driver.quit()
