import math

def solution(signals):
    cycles = [sum(s) for s in signals]
    lcm = 1
    for c in cycles:
        lcm = lcm * c // math.gcd(lcm, c)

    for t in range(1, lcm + 1):
        all_yellow = True
        for i, (g, y, r) in enumerate(signals):
            inter = (t - 1) % cycles[i]
            if not (g <= inter < g + y):
                all_yellow = False
                break
        if all_yellow:
            return t

    return -1