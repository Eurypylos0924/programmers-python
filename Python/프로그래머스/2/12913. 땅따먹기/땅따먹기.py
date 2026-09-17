def solution(land):
    n = len(land)
    for i in range(1, n):
        prev = land[i-1]
        best_idx = 0
        for k in range(1, 4):
            if prev[k] > prev[best_idx]:
                best_idx = k
        best = prev[best_idx]
        second = max(prev[k] for k in range(4) if k != best_idx)
        
        for j in range(4):
            land[i][j] += second if j == best_idx else best
    return max(land[-1])