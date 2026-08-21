def solution(my_string):
    answer = []
    l = len(my_string)
    for i in range(0,l):
        answer.append(my_string[-i::])
    answer.sort()
    return answer