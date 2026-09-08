def solution(a, b):
    a = a[::-1]  # 뒤집어서 낮은 자릿수부터 접근하기 쉽게
    b = b[::-1]
    
    result = []
    carry = 0
    
    for i in range(max(len(a), len(b))):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0
        
        total = digit_a + digit_b + carry
        result.append(str(total % 10))
        carry = total // 10
    
    if carry:
        result.append(str(carry))
    
    return "".join(result[::-1])