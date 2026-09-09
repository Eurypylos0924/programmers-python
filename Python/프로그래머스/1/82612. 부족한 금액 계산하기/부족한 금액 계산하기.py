def solution(price, money, count):
    total = price*(count+1)*count/2
    if total > money:
        answer = total-money
    else:
        answer = 0

    return answer