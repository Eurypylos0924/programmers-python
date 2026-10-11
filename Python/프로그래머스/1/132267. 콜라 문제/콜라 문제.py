def solution(a, b, n):
    answer = 0
    bottle = n
    
    while bottle >= a:
        exchanged = bottle//a
        answer += exchanged*b
        remain = bottle%a
        bottle = remain + exchanged*b
        
    return answer