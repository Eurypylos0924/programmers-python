from collections import Counter

def solution(str1, str2):
    def to_counter(s):
        return Counter([s[i:i+2].lower() for i in range(len(s)-1) if s[i:i+2].isalpha()])
    
    dict1, dict2 = to_counter(str1), to_counter(str2)
    a_sum = sum((dict1 & dict2).values())
    b_sum = sum((dict1 | dict2).values())
    
    if b_sum == 0:
        return 65536
    return int((a_sum / b_sum) * 65536)