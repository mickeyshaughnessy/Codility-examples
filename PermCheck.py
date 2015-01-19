def solution(A):
    euler = len(A) * (len(A) + 1) / 2
    B = set(A)
    if sum(A) == euler and len(set(A)) == len(A):
        return 1
    else:
        return 0
