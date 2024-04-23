class Solution:
	def sort(self, A):
		if not A:
			return A
		self.merge_sort(A, 0, len(A) -1)


    # [2, 1]
def mergeSort(self, A, start, end):
  if start >= end:
    return
  
  mid = (start + end) // 2
  self.mergeSort(A, start, mid)
  self.mergeSort(A, mid + 1, end)
  self.merge(A, start, mid, end)

def merge(self, A, start, mid, end):
  sorted_A = []
  left, right = start, mid + 1
  while left <= mid and right <= end:
    if A[left] < A[right]:
      sorted_A.append(A[left])
      left += 1
    else:
      sorted_A.append(A[right])
      right += 1	
  while left <= mid:
    sorted_A.append(A[left])
    left += 1
  while right <= end:
    sorted_A.append(A[right])
    right += 1
  # copy to original array
  for i in range(start, end + 1):
    A[i] = sorted_A[i - start]




	
