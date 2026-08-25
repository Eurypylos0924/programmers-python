def solution(n,a,b):
    answer = 1
    if a>b:
        a,b = b,a
    
    while not (b-a == 1 and a%2 == 1):
        if a%2 == 1:
            a = a//2 + 1
        else:
            a = a//2
        if b%2 == 1:
            b = b//2 + 1
        else:
            b = b//2
        answer += 1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer