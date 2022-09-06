from bs4 import BeautifulSoup
import requests

from MlbMatchup import MlbMatchup
from rankMatchups import dropTbdMatchups, rankMatchups

# load all html of our webpage
html_text = requests.get('https://www.mlb.com/probable-pitchers').text
soup = BeautifulSoup(html_text, 'lxml')
# container of all pitching matches
mlb_matchup_container = soup.find('div', class_='container')

# find current pitching matchup
mlb_matchup_list = mlb_matchup_container.find_all('div', class_='probable-pitchers__matchup')

ranked_matchups = []

for matchup in mlb_matchup_list:
    mlb_matchup = MlbMatchup(matchup)
    ranked_matchups.append(mlb_matchup)

# drop tbd (incomplete) matchup information
ranked_matchups = dropTbdMatchups(ranked_matchups)

# oder matchups from most favorable to least favorable
# ranked_matchups = rankMatchups(ranked_matchups)

