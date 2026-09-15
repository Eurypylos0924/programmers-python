def solution(numbers, target):
    answer = [0]
    n = len(numbers)
    
    def dfs(index, current_sum):
        if index == n:
            if current_sum == target:
                answer[0] += 1
            return
        
        dfs(index+1, current_sum + numbers[index])   # 이 숫자를 +로 쓰는 경우
        dfs(index+1, current_sum - numbers[index])   # 이 숫자를 -로 쓰는 경우
    
    dfs(0, 0)
    return answer[0]