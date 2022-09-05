from bs4 import BeautifulSoup
import requests

from PitchingMatchup import PitchingMatchup

# load all html of our webpage
html_text = requests.get('https://www.mlb.com/probable-pitchers').text
soup = BeautifulSoup(html_text, 'lxml')

# container of all pitching matches
pitching_matches_container = soup.find('div', class_='container')

# find current pitching matchup
pitching_match = pitching_matches_container.find('div', class_='probable-pitchers__matchup')

# gives us access to the team info
probable_pitchers_game = pitching_match.find('div', class_='probable-pitchers__game')

# code will strip the names of the pitchers
# probable_pitchers_team_names = probable_pitchers_game.find('div', class_='probable-pitchers__team-names')
probable_pitchers_team_name = probable_pitchers_game.find_all('span', class_='probable-pitchers__team-name')

matchup = PitchingMatchup(pitching_match)

# for i in team_name:
#     print(i.text.strip())

# extract the record from our pitching matchup to analyze further 
probable_pitchers_game_info = probable_pitchers_game.find('div', class_="probable-pitchers__game-info")
probable_pitchers_team_record = probable_pitchers_game_info.find_all('div', class_='probable-pitchers__team-record')

# create a print statement for game:
# at = probable_pitchers_team_name[1].text.strip()
# print(f'''{probable_pitchers_team_name[0].text.strip()} {at} {probable_pitchers_team_name[2].text.strip()}
# {probable_pitchers_team_record[0].text.strip()}   {probable_pitchers_team_record[1].text.strip()}''')

# print(probable_pitchers_team_record)


