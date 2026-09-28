def solution(s):
    s1 = s.split(' ')
    s1 = list(map(int,s1))
    maxnum = max(s1)
    minnum = min(s1)
    
    return f"{minnum} {maxnum}"