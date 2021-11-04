class Solution:

	def sort(self, A):
		self.quick_sort(A, 0, len(A) - 1)

    
    # start - the start index
    # end - the end index
	def quick_sort(self, A, start, end):

		if start >= end:
			return

		left, right = start, end

		pivot = A[(left + right) // 2]

		while left <= right:
			while left <= right and A[left] < pivot:
				left += 1

			while left <= right and A[right] > pivot:
				right -= 1

			if left <= right:
				A[left], A[right] = A[right], A[left]
				left += 1
				right -=1


		self.quick_sort(start, left)
		self.quick_sort(right, end)

