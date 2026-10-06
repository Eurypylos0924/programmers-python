def solution(storey):

    s = str(storey)[::-1]
    l = len(s)
    
    def dfs(idx,carry):
        if idx == l:
            return carry
        num = int(s[idx]) + carry
        remain = num%10
        cnt_carry = num//10
        down = remain + dfs(idx+1, cnt_carry)
        if remain != 0:
            up = (10-remain) + dfs(idx+1, cnt_carry+1)
        else:
            up = dfs(idx+1, cnt_carry)
            
        return min(down, up)
    
    return dfs(0,0)

