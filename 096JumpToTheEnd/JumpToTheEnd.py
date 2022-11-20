def hop_to_end(hopsFromPlaces):
    numberOfPlaces = len(hopsFromPlaces)
    roundsNecToReach = [i for i in range(0, numberOfPlaces)]
    for curPlace in range(0, numberOfPlaces):   # iterating through the list of places
        for hopTarget in range(curPlace + 1, min(curPlace + hopsFromPlaces[curPlace] + 1, numberOfPlaces)):
            roundsNecToReach[hopTarget] = min(roundsNecToReach[curPlace] + 1, roundsNecToReach[hopTarget])
    return roundsNecToReach[-1]
