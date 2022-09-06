from helpers import toText

class Pitcher():
    def __init__(self, name, stat_summary):
        self.name = name
        self.stat_summary = stat_summary
        self.wins = self.stat_summary.find('span', 'probable-pitchers__pitcher-wins')
        self.losses = self.stat_summary.find('span', 'probable-pitchers__pitcher-losses')
        self.era = self.stat_summary.find('span', 'probable-pitchers__pitcher-era')
        self.strikeouts = self.stat_summary.find('span', 'probable-pitchers__pitcher-so')

    def getName(self):
        return toText(self.name)

    def getWins(self):
        return toText(self.wins)
    
    def getLosses(self):
        return toText(self.losses)
    
    def getRecord(self):
        return (f'({self.getWins()}-{self.getLosses()})')

    def getEra(self):
        return toText(self.era)
    
    def getStrikeouts(self):
        return toText(self.strikeouts)
    
    def getStatsToString(self):
        if self.name != 'TBD':
            return f'''{self.getName()} {self.getRecord()}\n {self.getEra()}, {self.getStrikeouts()}'''
        else:
            return 'None'