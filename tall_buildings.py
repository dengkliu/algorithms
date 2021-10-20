# https://www.lintcode.com/problem/285/

# At the weekend, Xiao Q and his friends came to the big city for shopping. 
# There are many tall buildings.There are n tall buildings in a row, whose height is indicated by arr.
# Xiao Q has walked from the first building to the last one. 
# Xiao Q has never seen so many buildings, so he wants to know how many buildings can he see at the location of each building? 
# (When the height of the front building is greater than or equal to the back building, the back building will be blocked)

# Input:[5,3,8,3,2,5]
# Output:[3,3,5,4,4,4]
# Explanation:
# When Xiao Q is at position 0, he can see 3 tall buildings at positions 0, 1, and 2.
# When Xiao Q is at position 1, he can see  3 tall buildings at positions 0, 1, and 2.
# When Xiao Q is at position 2, he can see the building at position 0, 1 forward, and the building at position 3, 5 backward, plus the third building, a total of 5 buildings can be seen.
# When Xiao Q is at position 3, he can see 4 tall buildings in positions 2, 3, 4, and 5.
# When Xiao Q is at position 4, he can see 4 tall buildings in positions 2, 3, 4, and 5.
# When Xiao Q is at position 5, he can see 4 tall buildings in positions 2, 3, 4, and 5.


# 1. Brute force
#    For each building, get how many buildings you can see on the right and left
#    Start from next building, if you see a higher building than current highest building, the add the count
#    O(N^2)

class Solution:
    """
    @param arr: the height of all buildings
    @return: how many buildings can he see at the location of each building
    """

    def tallBuilding(self, arr):
        
        result = [1 for _ in range(len(arr))]

        for i in range(len(arr)):
            highest = 0
            right_buildings_count = 0
            for j in range(i + 1, len(arr)):
                if arr[j] > highest:
                    right_buildings_count += 1
                    highest = arr[j]
            result[i] += right_buildings_count
        
        for i in range(len(arr) - 1, -1, -1):
            highest = 0
            left_buildings_count = 0
            for j in range(i - 1, -1, -1):
                if arr[j] > highest:
                    left_buildings_count += 1
                    highest = arr[j]
            result[i] += left_buildings_count


        return result


# 2. Monotonic stack

class Solution:
    """
    @param arr: the height of all buildings
    @return: how many buildings can he see at the location of each building
    """

    def tallBuilding(self, arr):

    	# 当前位置的楼房一定可以看到
        result = [1 for _ in range(len(arr))]

        stack = []

        # 向左可以看到多少楼房
        # 可以看到的楼房 一定是一个单调递增的序列
        # 可以看到的楼房数量 就是这个序列的长度！！
        for i in range(len(arr)):
            result[i] += len(stack)
            while stack and stack[-1] <= arr[i]:
                stack.pop(-1)
            stack.append(arr[i])
        
        stack = []

        # 像右可以看到多少楼房
        for i in range(len(arr) - 1, -1, -1):
            result[i] += len(stack)
            while stack and stack[-1] <= arr[i]:
                stack.pop(-1)
            stack.append(arr[i])
        
        return result
        

      