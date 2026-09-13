def solution(numbers):
    answer = [-1] * len(numbers)
    cri = []
    for i in range(len(numbers)):
        while cri and numbers[cri[-1]] < numbers[i]:
            j = cri.pop()
            answer[j] = numbers[i]
        cri.append(i)
    
    return answer