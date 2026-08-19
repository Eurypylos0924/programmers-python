def solution(x, n):
    answer = []
    if x == 0:
        answer = [0]*n
    else:
        for i in range (x,x*(n+1),x):
            answer.append(i)
    return answer