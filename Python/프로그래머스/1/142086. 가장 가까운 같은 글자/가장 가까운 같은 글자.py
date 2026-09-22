def solution(s):
    answer = [-1]*(len(s))
    cri = {}
    
    for i in range(0,len(s)):
        if cri and s[i] in cri:
            for j in range(0,i):
                if s[i] == s[j]:
                    answer[i] = i-j
                    cri[s[i]] = i
                else:
                    continue
        else:
            cri[s[i]] = i
            
    return answer