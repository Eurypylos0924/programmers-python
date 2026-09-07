from itertools import product

def solution(word):
    wlist = []
    for i in range(1,6):
        raw = list(product('AEIOU', repeat=i))
        wlist += [''.join(x) for x in raw]
        wlist.sort()
    
    return wlist.index(word) + 1