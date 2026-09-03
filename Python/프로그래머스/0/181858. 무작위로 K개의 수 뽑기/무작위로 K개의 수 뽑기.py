def solution(arr, k):
    answer = []
    cri = []
    for i in range(len(arr)):
        if not cri or arr[i] not in cri:
            cri.append(arr[i])
    l = len(cri)

    if k >= l:
        answer = cri + [-1]*(k-l)
    else:
        answer = cri[0:k]
        
    return answer
