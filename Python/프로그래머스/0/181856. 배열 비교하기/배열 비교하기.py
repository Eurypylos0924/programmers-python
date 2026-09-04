def solution(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    
    if l2 > l1:
        return -1
    elif l1 > l2:
        return 1
    else:
        if sum(arr1) == sum(arr2):
            return 0
        elif sum(arr1) > sum(arr2):
            return 1
        else:
            return -1