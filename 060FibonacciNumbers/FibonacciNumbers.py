def generate_fibo(n):
    prevprev, prev = 0, 1
    for _ in range(2, n + 1):
        prevprev, prev = prev, prev + prevprev
    return prev
