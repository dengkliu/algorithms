
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.

class Solution:
    def countSmaller(self, nums):

        n = len(nums)
        # 1. How to get both value and index for each element in an array
        arr = [[value, index] for index, value in enumerate(nums)]
        result = [0] * n
        
        def mergeSort(arr, start, end):
            if start >= end:
                return
            mid = (start + end) // 2
            mergeSort(arr, start, mid)
            mergeSort(arr, mid + 1, end)
            merge(arr, start, mid, end)
        
        def merge(array, start, mid, end):
            # 2. Why do we keep an empty sorted array?
            sorted_array = []
            left, right = start, mid + 1
            while left <= mid and right <= end:
                if arr[left][0] <= arr[right][0]:
                    sorted_array.append(array[left])
                    # 3. Why do the addition here when left array element is samller?
                    result[arr[left][1]] += right - mid - 1
                    left += 1
                else:
                    sorted_array.append(array[right])
                    right += 1
            while left <= mid:
                sorted_array.append(array[left])
                result[arr[left][1]] += right - mid - 1
                left +=1
            while right <= end:
                sorted_array.append(array[right])
                right += 1
            
            # copy to original array
            for i in range(start, end + 1):
                array[i] = sorted_array[i - start]

        mergeSort(arr, 0, n - 1)
        return result
