# class to access attributes of pitching matchup
class PitchingMatchup():
    def __init__(self, pitching_match):
        self.game = pitching_match.find('div', class_='probable-pitchers__game')
        self.teams = self.game.find_all('span', class_='probable-pitchers__team-name')
        self.away_team_name = self.teams[0]
        self.home_team_name = self.teams[2]
        
    

    def getAwayTeamName(self):
        return self.away_team_name.text.strip()

    def getHomeTeamName(self):
        return self.home_team_name.text.strip()

    