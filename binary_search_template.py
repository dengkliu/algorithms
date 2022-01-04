# O(logN) time complexity

# Get the first occurence of the target
class binarySearch:

	def binary_search(self, nums, target):
		
		# make sure nums is not None or len(nums) == 0
		if nums is None:
			return -1

		start, end = 0, len(nums) - 1
		
		# start + 1 < end, to avoid infinite while loops
		# Sample [1, 1], target 1.
		# If use start < end, start will always be 0 and end will always be 1, mid will be always be 0.
		while start + 1 < end:
			# get the floor, python don't have overflow issue for integers
			# https://www.quora.com/How-is-there-no-integer-overflow-in-Python 
			mid = (start + end)//2
			
			if nums[mid] < target:
				start = mid
			elif nums[mid] == target:
				end = mid
			else:
				end = mid
				
	        # return the first occurrence of the target
		if nums[start] == target:
			return start
		if nums[end] == target:
			return end

		return -1


# Get the last occurence of the target
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        
        # Empty or None will be considered false in boolean context
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end)//2

            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                # move start close to the end, choose the right half
                start = mid
            else:
                end = mid
        
        # First check the end
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        return -1

