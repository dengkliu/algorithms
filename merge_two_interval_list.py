# https://leetcode.com/discuss/interview-question/124616/

# Given A and B two interval lists, A has no overlap inside A and B has no overlap inside B. Write the function to merge two interval lists, output the result with no overlap. Ask for a very efficient solution


def mergeInterval(self, A, B):
	ptr1, ptr2 = 0, 0
	merged_interval = []
	while ptr1 < len(A) or pt2 < len(B):
		if ptr1==len(A):
			curr = B[ptr2]
			ptr2 += 1
		elif ptr2 == len(B):
			curr = A[ptr1]
			ptr1 += 1
		elif A[ptr1][0] <= B[ptr1][0]:
			curr = A[ptr1]
			ptr1 += 1
		else:
			curr = B[ptr2]
			ptr2 += 1

		if merged_interval and merged_interval[-1][1] >= curr[0]:
			merged_interval[-1][1] = max(merged_interval[-1][1], curr[1])
		else:
			merged_interval.append(curr)

	return merged_interval