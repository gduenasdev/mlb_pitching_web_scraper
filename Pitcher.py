from utilities import toText

class Pitcher():
    def __init__(self, name = 'TBD', stat_summary = 'TBD'):
        self.name = name
        self.stat_summary = stat_summary
        self.wins = 'TBD'
        self.losses = 'TBD'
        self.era = 'TBD'
        self.strikeouts = 'TBD'

        self.setPitcherStats()
    
    def setPitcherStats(self):
        if self.stat_summary != 'TBD':
            self.wins = self.stat_summary.find('span', 'probable-pitchers__pitcher-wins')
            self.losses = self.stat_summary.find('span', 'probable-pitchers__pitcher-losses')
            self.era = self.stat_summary.find('span', 'probable-pitchers__pitcher-era')
            self.strikeouts = self.stat_summary.find('span', 'probable-pitchers__pitcher-so')

    def getName(self):
        if self.name == 'TBD':
            return self.name
        else:
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
            return 'TBD'