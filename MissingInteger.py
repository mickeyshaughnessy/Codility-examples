def solution(A):
    # find the smallest positive integer that does not appear in A.
    # eg. A = [1]  return 2
    #   A = [10,6,1,3,2] return 4
    #   A = [1,2,5,9] return 3
    # A = [9,1,6,4,1,45] return 2
    # A = [2,3] return 1
    # A = [5,3,2,1]
    
    counts = [0]*100001
    for i in A:
        if i < 1000001 and i > 0:
            counts[i-1] += 1
    
    index = 0
    for j in counts:
        index += 1
        if j == 0:
            print ('j is %s' % j)
            print ('index is %s' % index)
            return index

