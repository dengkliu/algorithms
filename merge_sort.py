class Solution:

	def sort(self, A):

		if not A:
			return A

		sorted_A = [0 for _ in range(len(A))]

		self.merge_sort(A, 0, len(A) -1, sorted_A)


    # [2, 1]
def mergeSort(A, start, end):
  if start >= end:
    return
  
  mid = (start + end) // 2
  mergeSort(A, start, mid)
  mergeSort(A, mid + 1, end)
  merge(A, start, mid, end)

def merge(A, start, mid, end):
  sorted_A = [0] * (end - start + 1)
  left, right = start, mid + 1
  index = 0
  while left <= mid and right <= end and index <= end - start:
    if start == 3 and end == 5:
      print(A[left])
      print(A[right])
    if A[left] < A[right]:
      sorted_A[index] = A[left]
      index += 1
      left += 1
    else:
      sorted_A[index] = A[right]
      index += 1
      right += 1	
  while left <= mid and index <= end - start:
    sorted_A[index] = A[left]
    left += 1
    index += 1
  while right <= end and index <= end - start:
    sorted_A[index] = A[right]
    right += 1
    index += 1
  # copy to original array
  for i in range(start, end + 1):
    A[i] = sorted_A[i - start]




	
