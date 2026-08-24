def solution(n, words):
    cri = []
    l = len(words)
    turn = 0
    failure = False
    
    for i in range(0,l):
        turn += 1
        if words[i] not in cri and (i==0 or words[i][0] == words[i-1][-1]):
            cri.append(words[i])
        else:
            failure = True
            break
            
    if failure:
        return [(turn-1)%n+1,(turn-1)//n+1]
    else:
        return [0,0]