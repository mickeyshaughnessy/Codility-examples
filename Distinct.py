def solution(A):
    if len(A) == 0:
        return 0
    A.sort()
    uniques = 1
    for i in range(0,len(A)-1):
        if A[i] != A[i+1]:
            uniques += 1
    return uniques
