from collections import deque

def solution(x, y, n):
    # BFS로 접근: x에서 시작해서, 한 번의 연산(+n, *2, *3)마다 "1단계"씩 퍼져나가며
    # y에 도달하는 최소 횟수를 찾는다 (BFS는 최단거리를 보장함)

    if x == y:
        return 0

    visited = [False] * (y + 1)   # 이미 큐에 넣어본 값인지 표시 (중복 방지)
    q = deque()
    q.append((x, 0))                # (현재값, 지금까지 연산 횟수)
    visited[x] = True

    while q:
        cur, cnt = q.popleft()

        for nxt in (cur + n, cur * 2, cur * 3):   # 세 가지 연산 결과 후보
            if nxt == y:
                return cnt + 1          # 목표에 도달했으니 이번이 마지막 연산
            if nxt < y and not visited[nxt]:
                # y보다 커지면 더 이상 의미 없음(더해도 곱해도 y로 못 돌아오니 가지치기)
                visited[nxt] = True
                q.append((nxt, cnt + 1))

    return -1   # 큐가 다 빌 때까지 y를 못 찾았다면 도달 불가능