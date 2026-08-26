def solution(want, number, discount):
    answer = 0
    shopdict = dict(zip(want,number))
    l = len(discount)

    cri = {}
    for x in range(0,10):
        if discount[x] in cri:
            cri[discount[x]] += 1
        else:
            cri[discount[x]] = 1
            
    if cri == shopdict:
        answer += 1
        
    for i in range(1,l-9):
        cri[discount[i-1]] -= 1
        if cri[discount[i-1]] == 0:
            del cri[discount[i-1]]
            
        if discount[i+9] in cri:
            cri[discount[i+9]] += 1
        else:
            cri[discount[i+9]] = 1
        
        if cri == shopdict:
            answer += 1
    
    return answer