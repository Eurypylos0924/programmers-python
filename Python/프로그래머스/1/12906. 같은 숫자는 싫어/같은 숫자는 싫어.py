def solution(arr):
    answer = [arr[0]]
    l = len(arr)
    for i in range(1,l):
        if answer and arr[i] != answer[-1]:
            answer.append(arr[i])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer