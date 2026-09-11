def solution(dirs):
    spot = (0, 0)
    direction = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    visited = set()
    
    for c in dirs:
        dx, dy = direction[c]
        nx, ny = spot[0] + dx, spot[1] + dy
        
        if abs(nx) < 6 and abs(ny) < 6:
            nspot = (nx, ny)
            visited.add(frozenset([spot, nspot]))
            spot = nspot
    
    return len(visited)