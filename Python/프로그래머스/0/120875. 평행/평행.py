def is_parallel(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    return (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1)

def solution(dots):
    p1, p2, p3, p4 = dots
    
    pairings = [(p1, p2, p3, p4),(p1, p3, p2, p4),(p1, p4, p2, p3)]
    for a, b, c, d in pairings:
        if is_parallel(a, b, c, d):
            return 1
    
    return 0