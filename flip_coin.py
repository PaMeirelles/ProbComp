def lcg(seed, a, c, m, n):
    x = seed
    u = []
    for _ in range(n):
        nx = ((a * x) + c) % m
        u.append(nx / m)
        x = nx
    return u

def flip_coin(n):
    if n > 0.5:
        return "head"
    else:
        return "tails"

def flip_pair(n1, n2):
    return [flip_coin(n1), flip_coin(n2)]

def simulation(seed, a, c, m, n):
    rand = lcg(seed, a, c, m, 2 * n)
    flips = [flip_pair(rand[i], rand[i+1]) for i in range(0,2 * n,2)]
    double_heads = [flip for flip in flips if flip == ["head", "head"]]

    print(f"We flipped {n} pairs of coins and got {len(double_heads)} double heads ({100 * len(double_heads) / n}%)")

    
    

simulation(1, 39373, 0, 2147483647, 10000)