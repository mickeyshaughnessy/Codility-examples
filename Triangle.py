def solution(A):
    if len(A) < 3:
        return 0
    A.sort()
    ind = 0
    for i in range(0,len(A)-2):
        if (A[i] + A[i+1] > A[i+2] and
                        A[i] + A[i+2] > A[i+1] and
                        A[i+1] + A[i+2] > A[i]
                    ):
            return 1
    return 0 
