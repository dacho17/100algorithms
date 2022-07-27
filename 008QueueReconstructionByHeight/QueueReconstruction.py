def reconstruct_queue(people):
    people.sort(key = lambda per: (-per[0], per[1]))

    res = []
    for person in people:
        res.insert(person[1], person)
    return res
