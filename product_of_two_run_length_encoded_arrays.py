# https://leetcode.com/problems/product-of-two-run-length-encoded-arrays

# Run-length encoding is a compression algorithm that allows for an integer array nums with many segments of consecutive repeated numbers to be represented by a (generally smaller) 2D array encoded. Each encoded[i] = [vali, freqi] describes the ith segment of repeated numbers in nums where vali is the value that is repeated freqi times.

# For example, nums = [1,1,1,2,2,2,2,2] is represented by the run-length encoded array encoded = [[1,3],[2,5]]. Another way to read this is "three 1's followed by five 2's".
# The product of two run-length encoded arrays encoded1 and encoded2 can be calculated using the following steps:

# Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
# Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i] * nums2[i].
# Compress prodNums into a run-length encoded array and return it.
# You are given two run-length encoded arrays encoded1 and encoded2 representing full arrays nums1 and nums2 respectively. Both nums1 and nums2 have the same length. Each encoded1[i] = [vali, freqi] describes the ith segment of nums1, and each encoded2[j] = [valj, freqj] describes the jth segment of nums2.

# Return the product of encoded1 and encoded2.

# Note: Compression should be done such that the run-length encoded array has the minimum possible length.

# Example 1:

# Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
# Output: [[6,6]]
# Explanation: encoded1 expands to [1,1,1,2,2,2] and encoded2 expands to [6,6,6,3,3,3].
# prodNums = [6,6,6,6,6,6], which is compressed into the run-length encoded array [[6,6]].


class Solution(object):
    def findRLEArray(self, encoded1, encoded2):
        """
        :type encoded1: List[List[int]]
        :type encoded2: List[List[int]]
        :rtype: List[List[int]]
        """
        nums1 = list(encoded1)
        nums2 = list(encoded2)

        p1, p2 = 0, 0
        result = []

        while p1 < len(nums1) and p2 < len(nums2):
            num1 = nums1[p1][0]
            fre1 = nums1[p1][1]
            num2 = nums2[p2][0]
            fre2 = nums2[p2][1]

            product = num1 * num2

            if fre1 < fre2:
                # why do we need this? 
                if result and product == result[-1][0]:
                    result[-1][1] += fre1
                else:
                    result.append([product, fre1])
                nums2[p2][1] = fre2 - fre1
                p1 += 1
            elif fre1 > fre2:
                if result and product == result[-1][0]:
                    result[-1][1] += fre2
                else:
                    result.append([product, fre2])
                nums1[p1][1] = fre1 - fre2
                p2 += 1
            else:
                if result and product == result[-1][0]:
                    result[-1][1] += fre1
                else:
                    result.append([product, fre1])
                p1 += 1
                p2 += 1

        
        return result