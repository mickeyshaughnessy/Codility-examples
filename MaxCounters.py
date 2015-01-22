def solution(N, A):
    
    counters = [0]*N
    cur_max = 0
    last_update = 0
    
    for op in A:
        if op == N+1:
            last_update = cur_max
        else:
            if counters[op-1] < last_update:
                counters[op-1] = last_update
            counters[op-1] += 1
            if counters[op-1] > cur_max:
                cur_max = counters[op-1]
        
    for i in range(len(counters)):
        if counters[i] < last_update:
            counters[i] = last_update
            
    return counters 
