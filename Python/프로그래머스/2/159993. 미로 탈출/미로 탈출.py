from collections import deque

def bfs(maps, start, n, m):

    dist = [[-1]*m for _ in range(n)]
    sr, sc = start
    dist[sr][sc] = 0
    q = deque()
    q.append((sr, sc))
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 'X' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    start = lever = exit_pos = None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit_pos = (i, j)

    dist_from_start = bfs(maps, start, n, m)
    to_lever = dist_from_start[lever[0]][lever[1]]
    if to_lever == -1:
        return -1

    dist_from_lever = bfs(maps, lever, n, m)
    to_exit = dist_from_lever[exit_pos[0]][exit_pos[1]]
    if to_exit == -1:
        return -1

    return to_lever + to_exit