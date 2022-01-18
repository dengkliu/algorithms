# https://www.lintcode.com/problem/1712/

# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
# A.length <= 30000 --> You should look for O(N) solution
# 0 <= S <= A.length
# A[i] is either 0 or 1.

class Solution:
    """
    @param A: an array
    @param S: the sum
    @return: the number of non-empty subarrays
    """
    def numSubarraysWithSum(self, A, S):
        prefix_sum = [0 for i in range(0, len(A) + 1)]
        sum_to_cnt = [0 for i in range(0, len(A))]
        sum_to_cnt[0] = 1

        result = 0
        
        for i in range(1, len(A) + 1):
            prefix_sum[i] = prefix_sum[i-1] + A[i-1]
            if prefix_sum[i] >= S:               
                result += sum_to_cnt[prefix_sum[i] - S]
            sum_to_cnt[prefix_sum[i]] += 1
          
        return result