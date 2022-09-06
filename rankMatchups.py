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

# will use merge sort to sort the matchups from most favorable to least
def rankMatchups(mlb_matchups):
    return mergeSort(mlb_matchups)

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if compareEra(left[i]) >= compareEra(right[j]):
              # The value from the left half has been used
              array[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                array[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1

# compare both pitchers era, must type cast from a string to a float to compare
# pitchers with no era will be '--.--' so we must except ValueErrors in this case
def compareEra(mlb_matchup):
    away_era = mlb_matchup.getPitcherInfo().getAwayPitcher().getEra().split(' ')
    home_era = mlb_matchup.getPitcherInfo().getHomePitcher().getEra().split(' ')

    try:
        away_era = float(away_era[0])
    except ValueError:
        away_era = 0.0
    
    try:
        home_era = float(home_era[0])
    except ValueError:
        home_era = 0.0

    return abs(away_era - home_era)