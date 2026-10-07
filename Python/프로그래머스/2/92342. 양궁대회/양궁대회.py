def distribute_gen(n_slots, n_picks):
    # 하나씩 생성(yield)하는 방식 -> 전체를 리스트로 안 쌓음
    if n_slots == 1:
        yield [n_picks]
        return
    for first in range(n_picks + 1):
        for rest in distribute_gen(n_slots - 1, n_picks - first):
            yield [first] + rest

def score(a,info):            
    asum = 0   # 어피치 점수
    rsum = 0   # 라이언 점수
    shooted = [False]*11
    
    for i in range(len(info)):
        if info[i]:
            shooted[i] = True
    resultlist = [x - y for x, y in zip(a, info)]
    
    for i in range(len(resultlist)):
        if resultlist[i] > 0:
            rsum += (10-i)
        elif resultlist[i] <= 0 and shooted[i] == True:
            asum += (10-i)

    return rsum - asum
            
def solution(n, info): 
    best_row = None
    best_score = float('-inf')  # 지금까지 본 것 중 최고 점수

    for a in distribute_gen(11, n):
        s = score(a,info)
        if s > best_score:          # 더 좋은 걸 찾으면 교체
            best_score = s
            best_row = a
        elif s == best_score and best_row is not None:
                # 점수차가 같으면: 낮은 점수(뒤쪽) 칸을 더 많이 맞힌 쪽 우선
                if a[::-1] > best_row[::-1]:
                    best_row = a
    
    if best_score <= 0:
        return [-1]
    
    return best_row