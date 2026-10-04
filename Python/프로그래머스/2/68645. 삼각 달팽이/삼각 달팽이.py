def solution(n):
    arr = [[0]*n for _ in range(n)]
    directions = [(1,0), (0,1), (-1,-1)] 
    row, col = 0, 0
    d = 0
    num = 1

    for i in range(n*(n+1)//2):
        arr[row][col] = num
        num += 1

        dr, dc = directions[d]
        next_row, next_col = row+dr, col+dc

        if not (0 <= next_row < n and 0 <= next_col <= next_row) or arr[next_row][next_col] != 0:
            d = (d+1) % 3
            dr, dc = directions[d]

        row, col = row+dr, col+dc

    answer = []
    for r in range(n):
        for c in range(r+1):
            answer.append(arr[r][c])
    return answer