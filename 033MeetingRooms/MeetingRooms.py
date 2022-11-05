def find_required_number_of_meetingrooms(lstOfIntervals):
    lstOfMoments = []   # list of tuples containing values (time, 1) or (time, -1) based on whether it was a starting or ending point of the meeting
    for interval in lstOfIntervals:
        lstOfMoments.extend([(interval[0], 1), (interval[1], -1)])

    lstOfMoments = sorted(lstOfMoments, key=lambda moment : (moment[0], moment[1]))

    roomsNeeded, roomsBeingUsed = 0, 0
    for moment in lstOfMoments:
        roomsBeingUsed += moment[1]
        if roomsBeingUsed > roomsNeeded:
            roomsNeeded = roomsBeingUsed
    
    return roomsNeeded
