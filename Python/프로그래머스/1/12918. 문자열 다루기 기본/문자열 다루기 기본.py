def solution(s):
    answer = True
    for i in s:
        if not i.isdigit():
            answer = False
        if len(s) != 4 and len(s) != 6:
            answer = False
    return answer