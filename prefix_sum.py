class PrefixSum:
    
    # prefixSum[i] = A[0] + A[1] + ... + A[i-1] the sum of first i numbers
    # sum from element A[i] to A[j] is prefixSum[j+1] - prefixSum[i]

    # int[] A =   [1, 2, 3, 4, 5];
    # prefixSum = [0, 1, 3, 6, 10, 15]

    // O(N)
   def getPrefixSum(self):
        prefix_sum = [0 for _ in range(len(A) + 1)]
        prefixSum[0] = 0
        
        for i in range(1, len(A) + 1):
            prefix_sum[i] = prefix_sum[i-1] + A[i-1]

        return prefixSum
