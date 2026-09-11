def solution(dirs):
    answer = 0
    spot = (0,0)
    direction = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}
    line = []
    
    for i in range(len(dirs)):
        if abs(spot[0] + direction[dirs[i]][0]) < 6 and abs(spot[1] + direction[dirs[i]][1]) < 6:
            nspot = (spot[0] + direction[dirs[i]][0], spot[1] + direction[dirs[i]][1])
            line.append(frozenset([spot,nspot]))
            spot = nspot
        else:
            continue

    return len(set(line))