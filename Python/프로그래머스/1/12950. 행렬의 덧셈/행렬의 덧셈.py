def solution(arr1, arr2):
    h = len(arr1)
    w = len(arr1[0])
    answer = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer