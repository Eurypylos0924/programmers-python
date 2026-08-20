import math

def solution(n):
    answer = 0
    for k in range(0,n//2+1):
        answer += math.comb(n-k,k)
    return answer%1234567