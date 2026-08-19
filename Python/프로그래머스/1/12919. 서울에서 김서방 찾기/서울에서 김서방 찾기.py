def solution(seoul):
    answer = ''
    for i,n in enumerate(seoul):
        if n == 'Kim':
            answer = i
    return f'김서방은 {answer}에 있다'