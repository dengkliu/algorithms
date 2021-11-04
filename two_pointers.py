# 1. pointers moving towards each other

# quick sort
def partition(self, A, start, end):
	
	if start >= end:
		return 

	left, right = start, end

	pivot = A[(start + end) // 2]

	# you should compare left <= right not left < right
	while left <= right:
		while left <= right and A[left] < pivot:
			left += 1

		while left<= right and A[right] > pivot:
			right -= 1

		if left <= right:
			A[left], A[right] = A[right], A[left]
			left += 1
			right -=1

	self.partition(A, start, left)
	self.partition(A, right, end)

# 2. pointers moving away from each other t

left, right = position, position + 1

while left >= 0 and right < len(A):

	if left and right can stop:
		break
	# left moves to the head of array
	left -=1
	# right moves to the end of array
	right += 1


# 3. pointers moving to the same direction

# you can use the logic if an only if - 
# when a subarray doesn't meet the requiement, all of its subarray doesn't meet the requirement
# initialize j as 0, j is the end of the subarray
end = 0 # we assume that end doesn't have to go back when start increase
# enumerate the start
for start in range(len(A)):
	while end < len(A) and the subarray between i and j does not meet the requirements
		end += 1

	if the subarray between start and end meets the requirements:
		handle the case here


# 4. pointers used to merge two arrays (used in merge sort)
def merge(self, list1, list2):
	new_list = []

	i, j = 0, 0

	while i < len(list1) and j < len(list2):
		if list1[i] < list2[i]:
			new_list.append(list1[i])
			i += 1
		else:
			new_list.append(list2[j])
			j += 1


	while i < len(list1):
		new_list.append(list1[i])
		i += 1

	while j < len(list2):
		new_list.append(list2[j])
		j += 1

	return new_list




