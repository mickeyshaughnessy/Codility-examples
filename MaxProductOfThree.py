def solution(A):
    A.sort()
    neg = A[0]*A[1]*A[-1]
    pos = A[-3]*A[-2]*A[-1]
    if neg > pos:
        return neg
    else:
        return pos
