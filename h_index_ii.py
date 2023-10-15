# https://leetcode.com/problems/h-index-ii/description/

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in ascending order, return the researcher's h-index.
# The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
# You must write an algorithm that runs in logarithmic time.

# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

# Input: citations = [1,2,100]
# Output: 2

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        start = 0
        end = len(citations) - 1

        while start + 1 < end:
            mid = (start + end)//2
            # If citations is less than the number of papers, it is NOT what we want
            # We have to further reduce the number of papers, which means we move further to the right part of the array
            if citations[mid] < (len(citations) - mid):
                start = mid
            else:
                end = mid
        
        # Here, a valid index is a index that is larger than the number of papers
        # If start is valid, end must be valid. Starting with start because it means more papers
        if citations[start] >= (len(citations) - start):
            return len(citations) - start
        elif citations[end] >= (len(citations) - end):
            return len(citations) - end
        else:
            return 0
