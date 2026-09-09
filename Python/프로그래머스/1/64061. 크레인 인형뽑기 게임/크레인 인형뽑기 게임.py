def nonzero(a):
    A = [x for x in a if x != 0]
    return A

def Trans(board):
    Y = list(map(list,zip(*board)))
    return Y
    
def solution(board, moves):
    answer = 0
    Y = Trans(board)
    NEW = [nonzero(col) for col in Y]
    save = []
    
    for i in moves:
        if NEW[i-1]:
            sel = NEW[i-1][0]
            NEW[i-1].pop(0)
        else:
            continue
        
        if save and save[-1] == sel:
            save.pop(-1)
            answer += 2
        else:
            save.append(sel)
        
    return answer

