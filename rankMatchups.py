# O(N) time as I iterate through the list once
# O(K) for the size of the slice forming a new array
def dropTbdMatchups(mlb_matchups):
    drop_tbd = 'TBD'
    start = 0
    end = len(mlb_matchups) - 1

    while start < end:
        while (start < end) and \
            (mlb_matchups[end].getPitcherInfo().getAwayPitcher().getName() == drop_tbd or \
            mlb_matchups[end].getPitcherInfo().getHomePitcher().getName() == drop_tbd):
            end -= 1
        if mlb_matchups[start].getPitcherInfo().getAwayPitcher().getName() == drop_tbd or \
            mlb_matchups[start].getPitcherInfo().getHomePitcher().getName() == drop_tbd:
            mlb_matchups[start], mlb_matchups[end] = mlb_matchups[end], mlb_matchups[start]
        start += 1
    return mlb_matchups[:end]

def rankMatchups(mlb_matchups):
    pass

def compareEra(mlb_matchup):
    pass

def compareRecord(mlb_matchup):
    pass