def change(num,n):    # 10진수를 n진수로 변환
    digits = '0123456789ABCDEF' # 미리 숫자를 0부터 15까지 원하는 표현과 매칭
    cng = ''
    if num == 0:
        return '0'
    else:
        while num:
            cng += digits[num % n] # n으로 나눈 나머지를 answer에 추가
            num //= n
    cng = cng[::-1]
    return str(cng)

def solution(n, t, m, p):
    answer = ''
    tot = t*m
    start = 0
    while len(answer) < tot:
        answer += change(start,n)
        start += 1
        
    answer = answer[0:tot]     # n진법 변화시 전체 길이가 길기 때문에 tot를 넘어서 answer형성 가능
        
    return answer[p-1::m]