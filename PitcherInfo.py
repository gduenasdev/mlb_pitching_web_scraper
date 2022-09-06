from Pitcher import Pitcher

# find pitchers information
class PitcherInfo():
    def __init__(self, mlb_matchup):
        self.pitcher_matchup = mlb_matchup.find('div', class_='probable-pitchers__pitchers')
        self.pitcher_names = self.pitcher_matchup.find_all('div', class_='probable-pitchers__pitcher-name')
        self.pitcher_stats = self.pitcher_matchup.find_all('div', class_='probable-pitchers__pitcher-stats-summary')
        self.away_pitcher = Pitcher(self.pitcher_names[0], self.pitcher_stats[0])
        self.home_pitcher = Pitcher(self.pitcher_names[1], self.pitcher_stats[1])
    
    def getAwayPitcherInfo(self):
        return self.away_pitcher

    def getHomePitcherInfo(self):
        return self.home_pitcher