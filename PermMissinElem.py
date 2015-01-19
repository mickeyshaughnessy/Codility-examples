def solution(A):
    euler = (len(A) + 1) * (len(A) + 2) / 2
    return euler - sum(A) 
