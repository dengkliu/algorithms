# https://www.lintcode.com/problem/360/

# Given an array of n integer, and a moving window(size k), 
# move the window at each iteration from the start of the array, 
# find the median of the element inside the window at each moving. 
# (If there are even numbers in the array, return the N/2-th number after sorting the element in the window. )

# Input:
# [1,2,7,8,5]
# 3
# Output:
# [2,7,7]

# Explanation:
# At first the window is at the start of the array like this `[ | 1,2,7 | ,8,5]` , return the median `2`;
# then the window move one step forward.`[1, | 2,7,8 | ,5]`, return the median `7`;
# then the window move one step forward again.`[1,2, | 7,8,5 | ]`, return the median `7`;