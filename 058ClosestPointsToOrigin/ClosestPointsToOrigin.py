import heapq

def efficient_calc_dist(x, y):
    return x*x + y*y

def k_closest_points(points, k):
    candidates = []
    for point in points:
        candidates.append((efficient_calc_dist(point[0], point[1]), point))
    heapq.heapify(candidates)

    sol = []
    [sol.append(heapq.heappop(candidates)[1]) for i in range(0, k)]
    return sol
