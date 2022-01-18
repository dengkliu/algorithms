// https://www.lintcode.com/problem/1712/

// In an array A of 0s and 1s, how many non-empty subarrays have sum S?
// A.length <= 30000 --> You should look for O(N) solution
// 0 <= S <= A.length
// A[i] is either 0 or 1.

// 1. Two pointers

public class Solution {
    /**
     * @param A: an array
     * @param S: the sum
     * @return: the number of non-empty subarrays
     */
    public int numSubarraysWithSum(int[] A, int S) {

        int end = 0, sum = 0, result = 0;

        if (A == null || A.length == 0) {
            return 0;
        }
            
        for (int start = 0; start < A.length; start ++) {

            // 假如S == 0，因为我们不允许empty subarray
            // 避免这种情况 我们先把end加进去
            if (S == 0) {
                sum += A[end];
                end ++;
            }

            while (end < A.length && sum < S) {
                sum += A[end];
                end ++;
            }

            // 如果到最后还是小于S
            // 不用往下继续找了
            if (sum < S) {
                break;
            }

            // 如果最后大于S，也不用找了，继续往下
            if (sum > S) {
                sum -= A[start];
                continue;
            }
            
            // 如果已经超出范围，那么只有这一个解，不用继续找了
            if (end == A.length) {
                result = result + 1;
                sum -= A[start];
                continue;
            }

            // 否则可以往后看看, 可以看看后面的end是不是0，这样可以有多个解
            int index = end;
            
            while (index < A.length) {
                if (A[index] == 0) {
                    index ++;
                    continue;
                } else {
                    break;
                }
            }

            result += index - end + 1;
        
            sum -= A[start];

        }

        return result;
    }
}

// 2. PrefixSum - Emuerate the end, for each end, how many start can meet the requirements?

public class Solution {
    /**
     * @param A: an array
     * @param S: the sum
     * @return: the number of non-empty subarrays
     */
    public int numSubarraysWithSum(int[] A, int S) {

        int[] prefixSum = new int[A.length + 1];
        int[] sumCnt = new int[A.length + 1];
        
        sumCnt[0] = 1;

        int result = 0;

        for (int i = 1; i < A.length + 1; i ++) {
            prefixSum[i] = prefixSum[i-1] + A[i-1];
            // You can only look at previous sums
             if (prefixSum[i] >= S) {
                result = result + sumCnt[prefixSum[i] - S];
            }
            sumCnt[prefixSum[i]]++;
        }

        return result;
    }
}