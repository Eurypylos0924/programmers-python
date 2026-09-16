def solution(sizes):
    answer = 0
    slist = list(map(sorted,sizes))
    newcri = list(zip(*slist))
    return max(newcri[0])*max(newcri[1])