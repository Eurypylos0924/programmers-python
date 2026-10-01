def solution(bandage, health, attacks):

    intv = bandage[0]
    totheal = bandage[0]*bandage[1] + bandage[2]
    l = len(attacks)
    hceil = health
    health -= attacks[0][1]
    if health <= 0:
        return -1
    
    for t in range(1,l):        
        if (attacks[t][0]-attacks[t-1][0]) <= intv:
            health += bandage[1]*((attacks[t][0]-attacks[t-1][0]-1)%intv)
            if health > hceil:
                health = hceil
            health -= attacks[t][1]
        else:
            health += totheal*((attacks[t][0]-attacks[t-1][0]-1)//intv)
            health += bandage[1]*((attacks[t][0]-attacks[t-1][0]-1)%intv)
            if health > hceil:
                health = hceil
            health -= attacks[t][1]
        if health <= 0:
            return -1
    return health

    print(totheal)
