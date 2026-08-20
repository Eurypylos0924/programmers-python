def solution(a, b, c, d):
    answer = 0
    numlist = [a,b,c,d]
    count = {}
    cri = set(numlist)
    length = len(cri)
    
    # 딕셔너리로 주사위 결과와 횟수 정리
    for num in numlist:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # 딕셔너리의 주사위 결과와 횟수 각각 리스트화
    keys = list(count.keys())
    values = list(count.values())
    
    if length == 1:
        answer = 1111*keys[0]
        
    elif length == 2:
        if 3 in values:           # 3개가 같은 값일때
            p = keys[values.index(3)]
            q = keys[values.index(1)]
            answer = (10*p+q)**2
        else:                     # 2개가 같은 값일때
            p = keys[0]
            q = keys[1]
            answer = (p+q)*abs(p-q)
            
    elif length == 3:
        p = keys[values.index(2)]
        answer = keys[0]*keys[1]*keys[2]//p
    else:
        answer = min(keys)
    
    return answer