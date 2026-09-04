def solution(cacheSize, cities):
    cache = {}
    cities = list(map(lambda x: x.lower(),cities))
    l = len(cities)
    citylist = []
    count = 0
    
    for i in range(l):
        if cacheSize == 0:
            count += 5
        
        elif cache and cities[i] in cache:
            cache[cities[i]] += 1
            citylist.remove(cities[i])
            citylist.append(cities[i])
            count += 1
            
        elif not cache:
            cache[cities[i]] = 1
            citylist.append(cities[i])
            count += 5
            
        elif cities[i] not in cache and len(list(cache.keys())) == cacheSize:
            del cache[citylist[0]]
            citylist.pop(0)
            citylist.append(cities[i])
            cache[cities[i]] = 1
            count += 5
            
        else:
            cache[cities[i]] = 1
            citylist.append(cities[i])
            count += 5
            
    return count