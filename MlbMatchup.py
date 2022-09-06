from GameInfo import GameInfo
from PitcherInfo import PitcherInfo

# class to access attributes of pitching matchup
class MlbMatchup():
    def __init__(self, mlb_matchup):
        self.game_info = GameInfo(mlb_matchup)
        self.pitcher_info = PitcherInfo(mlb_matchup)

    def getGameInfo(self):
        return self.game_info
    
    def getPitcherInfo(self):
        return self.pitcher_info
    
    def getMlbMatchupToString(self):
        game_info_string = self.getGameInfo().getGameInfoString()
        away_pitcher_string = self.getPitcherInfo().getAwayPitcher().getStatsToString()
        home_pitcher_string = self.getPitcherInfo().getHomePitcher().getStatsToString()
        
        return f'''{game_info_string}\n{away_pitcher_string}\n{home_pitcher_string}'''