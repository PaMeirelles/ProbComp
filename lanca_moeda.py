def lcg(seed, a, c, m, n):
    x = seed
    u = []
    for _ in range(n):
        nx = ((a * x) + c) % m
        u.append(nx / m)
        x = nx
    return u

print(lcg(1, 39373, 0, 2147483647, 10000))