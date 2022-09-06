from bs4 import BeautifulSoup
import requests

from MlbMatchup import MlbMatchup

# load all html of our webpage
html_text = requests.get('https://www.mlb.com/probable-pitchers').text
soup = BeautifulSoup(html_text, 'lxml')
# container of all pitching matches
mlb_matchup_container = soup.find('div', class_='container')

# find current pitching matchup
mlb_matchup = mlb_matchup_container.find('div', class_='probable-pitchers__matchup')

mlb = MlbMatchup(mlb_matchup)
print(mlb.getMlbMatchupToString())