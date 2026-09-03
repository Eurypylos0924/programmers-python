def solution(phone_book):
    answer = True
    l = len(phone_book)
    phone_book.sort()
    for i in range(l-1):
        cri = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][0:cri]:
            answer = False
        
    return answer