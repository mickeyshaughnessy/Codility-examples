def solution(A):
    sum_east = 0
    passes = 0
    for car in A:
        if car == 0:
            sum_east += 1
        if car == 1:
            passes += sum_east
    if passes > 1000000000:
        return -1
    return passes
