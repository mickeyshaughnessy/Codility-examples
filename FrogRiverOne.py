def solution(X, A):
    required = list(xrange(X)) 
    
    time = 0
    for leaf in A:
        if leaf - 1 in required:
            required.remove(leaf-1)
        if len(required) == 0:
            return time
        time += 1
    return -1
