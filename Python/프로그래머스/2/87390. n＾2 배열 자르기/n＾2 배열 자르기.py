def solution(n, left, right):
    answer = []
    
    length = right - left + 1
    s_x = left%n
    s_y = left//n
    e_x = right%n
    e_y = right//n
    
    if s_y == e_y:
        for i in range(s_x,e_x+1):
            answer.append(max([i,s_y])+1)
    
    else:
        for i in range(s_x,n):
            answer.append(max([i,s_y])+1)
            
        for j in range(s_y+1,e_y):
            for i in range(0,n):
                answer.append(max([i,j])+1)
        for i in range(0,e_x+1):
            answer.append(max([i,e_y])+1)

    return answer
