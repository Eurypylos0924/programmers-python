from itertools import combinations

def solution(numbers, target):
    comb = []
    sumlist = []
    totsum = sum(numbers)
    answer = 0
    
    for i in range(1,len(numbers)):
        comb.extend(combinations(numbers,i))
        
    for j in range(len(comb)):
        sumlist.append(sum(comb[j]))
        
    for x in range(len(sumlist)):
        if target == (totsum - (sumlist[x]*2)):
            answer += 1
    
    return answer