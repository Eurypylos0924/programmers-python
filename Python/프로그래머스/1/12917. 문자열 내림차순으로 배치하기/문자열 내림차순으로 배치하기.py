def solution(s):
    answer = ''
    front = [ y for y in s if y == y.lower()]
    back = [ x for x in s if x == x.upper()]
    front.sort(reverse=True)
    back.sort(reverse=True)

    answer = front + back
    return ''.join(answer)