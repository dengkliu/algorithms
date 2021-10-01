# https://www.lintcode.com/problem/1861/

# There is a mouse jumping from the top of a staircase with height n. 
# This mouse can jump 1, 3 or 4 steps in an even number of jumps and 1, 2, or 4 steps in an odd number of times. 
# Some steps have glue,if the mouse jump those steps,it will be directly stuck and cannot continue to jump.
# You need to solve how many ways the mouse can reach the ground ( level 0 ) from the top of this staircase.
# It also can be reached if it exceeds the ground. For example, jumping from 1 to -1 is another plan for jumping from 1 to 0.
# The state of the stairs with or without glue is input from high to low, that is, arr[0] is the top of the stairs.
# arr[i] == 0 represents that there is no glue on the i-th position, arr[i] == 1 represents that there is glue on the i-th position.

class Solution:
    """
    @param arr: the steps whether have glue
    @return: the sum of the answers
    """
    # dp[i][j] -- how many ways to reach j if i steps are taken
    # [0, 0, 0]
    #   0 1 2 3 4 5
    # 0 1 0 0 0 0 0
    # 1 0 1 1 0 1 0
    # 2 0 0 1 0 1 1
    def ratJump(self, arr):
        MOD = 10**9 + 7
        # Write your code here.
        if not arr or len(arr) == 0:
            return 0

        n = len(arr)

        # 0 1 2 3 n == 4
        # 0 1 2 3 4 5 6 
        # maximum the rats can go to index n + 2
        # maximum the rats need to take n - 1 steps
        dp = [[0 for _ in range(n + 3)] for _ in range(n)]

        if (arr[0] == 1):
            return 0

        dp[0][0] = 1
        dp[1][1] = 1
        dp[1][2] = 1
        dp[1][4] = 1

        for stair in (1, n + 3):
            if stair == 1 or stair == 2 or stair == 4:
                dp[1][stair] = 1

        for step in range(2, n):
            for stair in range(2, n + 3):

                if stair < n and arr[stair] == 1: 
                    continue
                
                # 走了奇数步
                # 之前可能在的位置是 stair - 1 stair - 2 和 stair - 4
                if (step%2 == 1):
                    if stair > 1 and stair - 1 < n - 1 and arr[stair - 1] == 0:
                        dp[step][stair] += dp[step - 1][stair - 1]
                    if stair > 2 and stair - 2 < n - 1 and arr[stair - 2] == 0:
                        dp[step][stair] += dp[step - 1][stair - 2] 
                    if stair > 4 and stair - 4 < n - 1 and arr[stair - 4] == 0:
                        dp[step][stair] += dp[step - 1][stair - 4]
                    dp[step][stair] %= MOD
                # 走了偶数步，之前的位置在哪里
                else:
                    if stair > 1 and stair - 1 < n - 1 and arr[stair - 1] == 0:
                        dp[step][stair] += dp[step - 1][stair - 1]
                    if stair > 3 and stair - 3 < n - 1 and arr[stair - 3] == 0:
                        dp[step][stair] += dp[step - 1][stair - 3]
                    if stair > 4 and stair - 4 < n - 1 and arr[stair - 4] == 0:
                        dp[step][stair] += dp[step - 1][stair - 4]
                    
        result = 0

 #       for i in range(n):
 #           print("-----")
 #           for j in range(n + 3):
 #               print(dp[i][j])

        for i in range(n):
            for j in range(n - 1, n + 3):
                result += dp[i][j]

        return result%MOD