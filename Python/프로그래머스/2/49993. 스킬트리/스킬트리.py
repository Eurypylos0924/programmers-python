def solution(skill, skill_trees):
    answer = 0
    criteria = []
    
    slist = [n for n in skill]
    
    for order in skill_trees:
        cri = [x for x in order if x in slist]
        joined = ''.join(cri)    
        if skill[0:len(joined)] == joined:
            answer += 1
    
    return answer