def fibonacci(n):
    return 1 if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

def climbing_combinations(target):
    prev, prevprev, curCombs = 1, 1, 1    
    for _ in range(2, target + 1):
        curCombs = prev + prevprev
        prevprev, prev = prev, curCombs

    return curCombs
