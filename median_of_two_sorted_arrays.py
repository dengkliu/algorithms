# https://www.lintcode.com/problem/65/description
# There are two sorted arrays A and B of size m and n respectively. 
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log(m + n)).

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):

        # if not A and not B:
        #     return - 1
        
        # if not A:
        #     return self.__find_median(B)

        # if not B:
        #     return self.__find_median(A)

        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        
        # 1 2 3 | 4 5 6 --> len 6 
        # 2 3 | 4  --> len 4 
        # mid = 2 
        # index_B = 5 - 2 - 2

        # 1 2 2 3 3 4 4 5 5 6

        # for even length, find n//2 and n//2 + 1 number
        # for odd length, find n//2 + 1 number
        # anyway, you want to make sure you have n//2 numbers on one side
        
        total_length = len(A) + len(B)

        if total_length%2 == 0:
            left_cnt = total_length//2
        else:
            left_cnt = total_length//2 + 1

        # you can have from 0 to len(A) numbers on partition A
        start, end = 0, len(A)            

        # start and end should merge
        while start <= end:
            cnt_A = (start + end)//2 
            cnt_B = left_cnt - cnt_A

            left_A = float('-inf') if cnt_A == 0 else A[cnt_A - 1]
            right_A = float('inf') if cnt_A == len(A) else A[cnt_A]

            left_B = float('-inf') if cnt_B == 0 else B[cnt_B - 1]
            right_B = float('inf') if cnt_B == len(B) else B[cnt_B]
    
            if left_A <= right_B and left_B <= right_A:
                if total_length%2 == 0:
                    return (max(left_A, left_B) + min(right_A, right_B))/2
                else:
                    return max(left_A, left_B)
            elif left_A > right_B:
                end = cnt_A - 1
            else:
                start = cnt_A + 1
        
        return -1

    def __find_median(self, A):
        if len(A)%2 == 0:
            return (A[len(A)//2 - 1] + A[len(A)//2])/2
        else:
            return A[len(A)//2]