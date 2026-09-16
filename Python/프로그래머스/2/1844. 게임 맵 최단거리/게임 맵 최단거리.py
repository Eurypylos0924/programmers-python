from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    maps[0][0] = 1
    
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))
    
    if not visited[n-1][m-1]:
        return -1
    return maps[n-1][m-1]