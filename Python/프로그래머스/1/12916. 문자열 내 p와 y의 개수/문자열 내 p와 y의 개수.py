def solution(s):
    answer = True
    num_p = 0
    num_y = 0
    wordlist = list(s.lower())
    for n in wordlist:
        if n == 'p':
            num_p += 1
        elif n == 'y':
            num_y += 1
        
    if num_p != num_y:
        answer = False

    return answer