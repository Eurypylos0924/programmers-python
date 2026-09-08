from collections import Counter

def solution(str1, str2):
    answer = 0
    
    dict1 = Counter([(str1[i]+str1[i+1]).lower() for i in range(0,len(str1)-1) if (str1[i]+str1[i+1]).isalpha()])
    dict2 = Counter([(str2[i]+str2[i+1]).lower() for i in range(0,len(str2)-1) if (str2[i]+str2[i+1]).isalpha()])
    
    a = dict1 & dict2   # 교집합
    b = dict1 | dict2   # 합집합
    a_sum = sum(list(a.values()))
    b_sum = sum(list(b.values()))
    
    if dict1 == dict2:
        return 65536
    else:
        return ((a_sum/b_sum)*65536)//1   
    