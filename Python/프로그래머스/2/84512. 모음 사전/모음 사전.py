def order(n):
    return 'AEIOU'.index(n)   # A=0, E=1, I=2, O=3, U=4

def solution(word):
    answer = 0
    l = len(word)
    for i in range(l):
        remain = 5 - (i+1)
        # 이 자리를 order(word[i])개의 "더 앞선 문자"로 바꿨을 때, 뒤에 자유롭게 오는 경우 다 더함
        for r in range(remain+1):
            answer += order(word[i]) * (5**r)
        # 지금까지(word[0]~word[i])는 그대로 두고, 이 자리에서 끝나는 경우 (1가지)
        answer += 1
    return answer