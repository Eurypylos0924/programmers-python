def solution(n):
    answer = ''
    result = 0
    while n > 0:
        n, m = divmod(n,3)
        answer += str(m)
    
    for i in range(len(answer)):
        result += int(answer[-1-i])*(3**i)
        
    return result