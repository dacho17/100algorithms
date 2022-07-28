def can_be_inclining(points):
    point_moved, length = False, len(points)
    for i in range(0, length - 1):
        if points[i] > points[i + 1]:
            if point_moved:     # if some point has already been pushed down
                return False
            elif i == 0:
                points[i] = points[i + 1] - 1   # push the point down, to has value less than the next
            elif i + 1 == length - 1:
                points[i + 1] = points[i] + 1   # push the last point in the list up, to have value larger than the prev
            elif points[i + 1] >= points[i - 1]:
                points[i] = points[i + 1]       # push the current point up, to have value between next and prev (same as next)
            else:
                return False
            point_moved = True
    return True
