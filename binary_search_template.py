# O(logN) time complexity

class binarySearch:

	def binary_search(self, nums, target):
		
		# make sure nums is not None or len(nums) == 0
		if nums is None:
			return -1

		start, end = 0, len(nums) - 1
		
		# start + 1 < end, to avoid infinite while loops
		# Sample [1, 1], target 1. Start will always be 0 and end will be 1, mid will be always be 0.
		while start + 1 < end:
			# get the floor
			mid = (start + end)//2
			
			if nums[mid] < target:
				start = mid
			elif nums[mid] == target:
				end = mid
			else:
				end = mid

		if nums[start] == target:
			return start
		if nums[end] == target:
			return end

		return -1
