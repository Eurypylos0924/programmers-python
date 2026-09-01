def multiply(arr1,arr2,i,j,w1):
    count = 0
    for x in range(w1):
        count += arr1[i][x] * arr2[x][j]
    return count

def solution(arr1, arr2):
    h1 = len(arr1)
    w1 = len(arr1[0])
    h2 = len(arr2)
    w2 = len(arr2[0])
    answer = [[0]*w2 for _ in range(h1)]
    
    for i in range(h1):
        for j in range(w2):
            answer[i][j] = multiply(arr1,arr2,i,j,w1)
    
    return answer
