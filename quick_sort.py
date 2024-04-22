class Solution:
	
	def sort(self, A):
		self.quick_sort(A, 0, len(A) - 1)
		
# start - the start index
# end - the end index
    def quickSort(self, A, start, end):
		if start >= end:
			return
		left, right = start, end
		pivot = A[(left + right) // 2]
		while left + 1 < right:
			while left + 1 < right and A[left] < pivot:
				left += 1
			while left + 1 < right and A[right] > pivot:
				right -= 1
			if left + 1 < right:
				A[left], A[right] = A[right], A[left]
				left += 1
				right -=1
		
		self.quickSort(A, start, left)
		self.quickSort(A, right, end)
