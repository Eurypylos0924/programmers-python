def solution(arr):
    l = len(arr)
    for i in range(0,11):
        cri = 0
        if l <= 2**i:
            cri += 2**i
            break
            
    return arr + [0]*(cri - l)