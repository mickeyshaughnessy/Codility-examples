def solution(X, A):
    counts = [0] * (X + 1)
    time = 0
    euler = 0
    for i in A:
        if i <= X:
            if counts[i] == 0: 
                euler += i
            counts[i] += 1
        if euler == X * (X + 1) / 2:
            return time
        time += 1
    return -1
