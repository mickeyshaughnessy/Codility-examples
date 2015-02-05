# The idea is to construct the prefix sum arrays (four of them) containing the numbers of 
# each nucleotide up to jth position
# Then, the difference between the pre- and post-sums for positions p and q are the numbers of
# nucleotides in the region.
# For these four differences, add the minimum impact factor

def solution(S, P, Q):
    impacts = {'A':1, 'C':2, 'G':3, 'T':4}
    
    sums = [[0]*len(S), [0]*len(S), [0]*len(S), [0]*len(S)] 
    
    
    for i in range(0,len(S)):
        if S[i] == 'A':
            sums[0][i] += 1
        if S[i] == 'C':
            sums[1][i] += 1    
        if S[i] == 'G':
            sums[2][i] += 1
        if S[i] == 'T':
            sums[3][i] += 1
            
        if i < len(S) - 1:
            for j in range (0,4):
                sums[j][i+1] = sums[j][i]
                    
    results = []            
    for n in range(0,len(P)):
        l = P[n]
        r = Q[n]
        
        pre_sum = [0,0,0,0]
        if l > 0:
            pre_sum = [sums[0][l-1], sums[1][l-1], sums[2][l-1], sums[3][l-1]]
        post_sum = [sums[0][r], sums[1][r], sums[2][r], sums[3][r]]
        
        if post_sum[0] - pre_sum[0] > 0: #There is an 'A'
            results.append(1)
        elif post_sum[1] - pre_sum[1] > 0: #There is an 'C'
            results.append(2)
        elif post_sum[2] - pre_sum[2] > 0: #There is an 'G'
            results.append(3)
        elif post_sum[3] - pre_sum[3] > 0: #There is an 'G'
            results.append(4)
        else:
            results.append(impact[S[n]])
    return results
