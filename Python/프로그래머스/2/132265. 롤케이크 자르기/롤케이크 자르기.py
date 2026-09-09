from collections import Counter

def solution(topping):
    answer = 0
    l = len(topping)
    back = Counter(topping)
    front = {}
      
    for i in range(l):
        if back[topping[i]] == 1:
            del back[topping[i]]
        else:
            back[topping[i]] -= 1
            
        if front and topping[i] in front:
            front[topping[i]] += 1
        else:
            front[topping[i]] = 1
            
        if len(front) == len(back):
            answer += 1

    return answer