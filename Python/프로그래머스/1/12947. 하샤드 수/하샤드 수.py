def solution(x):
    answer = False
    numlist = list(str(x))
    num = sum(map(int,numlist))
    if x%num == 0:
        answer = True
    return answer