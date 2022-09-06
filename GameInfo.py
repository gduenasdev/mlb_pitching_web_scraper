from utilities import toText
# gives us access to the team info
# code will strip the names of the pitchers
# extract the record from our pitching matchup to analyze further 
# create a print statement for game:

class GameInfo():
    def __init__(self, pitching_match):
        self.pitching_match = pitching_match
        self.team_matchup = pitching_match.find('div', class_='probable-pitchers__game')
        self.team_names = self.team_matchup.find_all('span', class_='probable-pitchers__team-name')
        self.away_team_name = self.team_names[0]
        self.home_team_name = self.team_names[2]
        self.game_info = self.team_matchup.find('div', class_="probable-pitchers__game-info")
        self.team_records = self.game_info.find_all('div', class_='probable-pitchers__team-record')
        self.away_team_record = self.team_records[0]
        self.home_team_record = self.team_records[1]
    
    def getAwayTeamName(self):
        return toText(self.away_team_name)

    def getHomeTeamName(self):
        return toText(self.home_team_name)

    def getAwayTeamRecord(self):
        return toText(self.away_team_record)
    
    def getHomeTeamRecord(self):
        return toText(self.home_team_record)
    
    def getGameInfoString(self):
        return f'''{self.getAwayTeamName()} @ {self.getHomeTeamName()}\n''' + \
        f'''{self.getAwayTeamRecord()}   {self.getHomeTeamRecord()}'''
    
    def printGameInfo(self):
        print(self.getGameInfoString())