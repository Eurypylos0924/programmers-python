from collections import Counter

def solution(clothes):
    answer = 1
    cl_kind = [x[1] for x in clothes]
    cl_dict = Counter(cl_kind)
    
    for i in cl_dict.values():
        answer = answer*(i+1)
    
    return answer-1