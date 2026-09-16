def structure(l):
    stru = []
    for i in range(l-1,-1,-1):
        stru.append(i)
    return stru    

def solution(prices):
    index = []
    l = len(prices)
    answer = structure(l)
    
    for i in range(l):
        while index and prices[index[-1]] > prices[i]:
            answer[index[-1]] = i-index[-1]
            index.pop(-1)
        index.append(i)
    
    return answer