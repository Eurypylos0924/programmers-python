def solution(progresses, speeds):
    cri = 0
    count = 0
    answer = []
    turncount = [((99-x+y)//y) for x,y in zip(progresses, speeds)]
    
    for i in range(len(turncount)):
        if i == 0:
            cri = turncount[0]
            count += 1
        elif cri >= turncount[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
            cri = turncount[i]
    answer.append(count)
    
    return answer 