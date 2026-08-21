def solution(arr):
    answer = []
    small = min(arr)
    if len(arr) == 1:
        answer = [-1]
    else:
        for i,v in enumerate(arr):
            if arr[i] == small:
                arr.pop(i)
                break
            answer = arr
    return answer