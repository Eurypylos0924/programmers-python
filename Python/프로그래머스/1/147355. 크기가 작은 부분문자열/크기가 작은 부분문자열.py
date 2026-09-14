def solution(t, p):
    answer = 0
    l = len(t)
    for i in range(0,l-(len(p)-1)):
        if t[i:i+len(p)] <= p:
            answer += 1
        
    return answer