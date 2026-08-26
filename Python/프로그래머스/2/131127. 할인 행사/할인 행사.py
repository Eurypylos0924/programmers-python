def solution(want, number, discount):
    answer = 0
    shopdict = dict(zip(want,number))
    for i in range(0,len(discount)-9):
        cri = {}
        for x in range(i,i+10):
            if discount[x] in cri:
                cri[discount[x]] += 1
            else:
                cri[discount[x]] = 1
        if cri == shopdict:
            answer += 1
    return answer