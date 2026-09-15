from collections import Counter

def solution(d, budget):
    cri = 0
    budlist = sorted(d)
    answer = 0
    
    for i in range(len(d)):
        if cri + budlist[i] > budget:
            break
        cri += budlist[i]
        answer += 1
            
    return answer