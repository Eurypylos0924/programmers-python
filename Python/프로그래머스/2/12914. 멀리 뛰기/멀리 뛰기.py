def solution(n):
    if n >= 3:
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, (a + b) % 1234567
    else:
        b = n % 1234567           
    return b