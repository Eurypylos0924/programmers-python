def solution(elements):
    ele = elements * 2
    l = len(elements)
    answer = set()
    
    for n in range(1, l+1):          # 부분수열 길이
        total = sum(ele[:n])          # 첫 구간의 합만 한 번 계산
        answer.add(total)
        for i in range(1, l):          # 그 다음부터는 슬라이딩
            total = total - ele[i-1] + ele[i+n-1]   # 앞의 원소 빼고, 뒤의 원소 더함
            answer.add(total)
    
    return len(answer)