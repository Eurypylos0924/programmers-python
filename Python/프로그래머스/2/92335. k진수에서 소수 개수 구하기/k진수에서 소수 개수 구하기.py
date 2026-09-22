def solution(n, k):
    
    def to_k(num, base):
        number = ''
        if num == 0:
            return '0'
        while num > 0:
            number += str(num % base)
            num //= base
        return number[::-1]

    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True

    k_num = to_k(n, k)          # n을 k진수 문자열로 변환 (예: "21102010 11" 같은 형태)
    tokens = k_num.split('0')    # '0'을 기준으로 쪼개면, 0 사이사이에 있던 숫자 덩어리들만 남음
                                  # (0P0, P0, 0P, P 형태가 전부 '0'으로 구분된 덩어리이므로)

    answer = 0
    for t in tokens:
        if t == '':              # 연속된 0이거나 맨 앞/뒤가 0이라 빈 문자열이 생긴 경우는 건너뜀
            continue
        if is_prime(int(t)):     # 그 덩어리를 10진법 정수로 보고 소수인지 판별
            answer += 1

    return answer