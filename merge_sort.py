class Solution:

	def sort(self, A):

		if not A:
			return A

		sorted_A = [0 for _ in range(len(A))]

		self.merge_sort(A, 0, len(A) -1, sorted_A)


    # [2, 1]

	def merge_sort(self, A, start, end, sorted_A):

		if start >= end:
			return

		mid = (start + end) // 2
		# handle from start to mid
		self.merge_sort(start, mid)
		# handle from mid + 1 to end
		self.merge_sort(mid + 1, end)
		
		self.merge(A, start, end, sorted_A)


	def merge(self, A, start, end, sorted_A):

		mid = (start + end) // 2

		left, right = start, mid + 1

		index = start

		while left <= mid and right <= end:
			if A[left] > A[right]:
				sorted_A[index] = A[left]
				index += 1
				left += 1
			else:
				sorted_A[index] = A[right]
				index += 1
				right += 1


		while left <= mid:
			sorted_A[index] = A[left]
			left ++

		while right <= end:
			sorted_A[index] = A[right]
			right ++

		for i in range(start, end + 1):
			A[i] = sorted_A[i]




	