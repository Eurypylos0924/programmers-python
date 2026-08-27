def solution(s):
    answer = 0
    l = len(s)
    A = ('(', '[', '{')
    B = (')', ']', '}')
    pair = dict(zip(A,B))
    
    for x in range(0,l):
        cri =[]
        s_new = s[x::] + s[0:x]
        for i in range(0,l):
            if cri and cri[-1] in A and pair[cri[-1]] == s_new[i]:
                cri.pop()
            else:
                cri.append(s_new[i])
        if cri == []:
            answer += 1
            
    return answer