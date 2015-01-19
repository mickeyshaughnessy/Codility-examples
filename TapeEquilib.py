def solution(A):
    B = []
    best_dif = 100000000000
    sum = 0
    for i in A:
        sum += i
    sum_left = 0
    sum_right = sum
    for i in A[:-1]:
        sum_left += i
        sum_right -= i
        dif = abs(sum_left - sum_right)
        if dif < best_dif:
            best_dif = dif
    return best_dif
