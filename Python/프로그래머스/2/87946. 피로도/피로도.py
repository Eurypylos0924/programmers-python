def count_d(k,order):
    fatigue = k
    count = 0
    for di in order:
        minfat = di[0]
        usage = di[1]
        if fatigue >= minfat:
            fatigue -= usage
            count += 1
    return count    
 
 

def solution(k, dungeons):
    l = len(dungeons)
    visited = [False]*l
    answer = [0]
 
    def dfs(fatigue, count):
        answer[0] = max(answer[0], count)
 
        for i in range(l):
            if not visited[i] and fatigue >= dungeons[i][0]:
                visited[i] = True
                dfs(fatigue - dungeons[i][1], count + 1)
                visited[i] = False
 
    dfs(k, 0)
 
    return answer[0]