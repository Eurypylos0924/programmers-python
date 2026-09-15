from itertools import combinations

def solution(number):
    answer = 0
    comb = list(combinations(number,3))
    
    for i in range(len(comb)):
        if sum(comb[i]) == 0:
            answer += 1
            
    return answer