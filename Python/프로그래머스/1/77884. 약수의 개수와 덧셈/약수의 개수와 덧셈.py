def sumFactors(num):
    factors = {}
    d = 2
    r = 1
    while d*d <= num:
        while num%d == 0:
            factors[d] = factors.get(d,0) + 1
            num //= d
        d += 1
            
    if num > 1:
        factors[num] = factors.get(num,0) + 1
        
    result =  list(factors.values())   
        
    for n in result:
        r *= (n+1)
        
    return r

def solution(left, right):
    answer = 0
    for i in range(left,right + 1):
        if sumFactors(i)%2 == 0:
            answer += i
        else: 
            answer -= i
    return answer