# https://www.lintcode.com/problem/1431/

# There are N dominoes in a line, and we place each domino vertically upright.
# In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left.
# Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
# Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
# Return a string representing the final state.

class Solution:
    """
    @param dominoes: a string
    @return: a string representing the final state
    """
    # for every second, only look at the dominoe that stays still
    # dp[i][j] = . if dp[i-1][j-1] == L dp[i-1][j+1] == R
    # dp[i][j] = L if dp[i-1][j-1] != R dp[i-1][j+1] == L
    # dp[i][j] = R if dp[i-1][j-1] == R dp[i-1][j+1] != L
    # 但是 不知道i有多少层,最多Len(dominoes)
    def pushDominoes(self, dominoes):
        # Write your code here
        
        n = len(dominoes)

        dp = [[0] * n for i in range(2)]

        # Initialize
        for i in range(n):
            if dominoes[i] == 'L':
                dp[0][i] = 1
            elif dominoes[i] == 'R':
                dp[0][i] = -1
            else:
                dp[0][i] = 0
        
        total_seconds = 0

        for i in range(1, n):
            total_seconds += 1
            same_as_prev_row = True

            if dp[(i-1)%2][0] == 1 or dp[(i-1)%2][0] == -1:
                dp[i%2][0] =  dp[(i-1)%2][0] 
            elif dp[(i-1)%2][1] == 1:
                dp[i%2][0] = 1
            
            if dp[(i-1)%2][n-1] == 1 or dp[(i-1)%2][n-1] == -1:
                dp[i%2][n-1] = dp[(i-1)%2][n-1] 
            elif dp[(i-1)%2][n-2] == -1:
                dp[i%2][n-1] = -1

            for j in range(1, n-1):
                if dp[(i-1)%2][j] == -1 or dp[(i-1)%2][j] == 1:
                    dp[i%2][j] = dp[(i-1)%2][j]
                    continue
                
                if dp[(i-1)%2][j-1] == 1 and dp[(i-1)%2][j+1] == -1:
                    continue
                    
                # 向左倒
                if dp[(i-1)%2][j-1] != -1 and dp[(i-1)%2][j+1] == 1:
                    dp[i%2][j] = 1
                
                # 向右倒
                if dp[(i-1)%2][j-1] == -1 and dp[(i-1)%2][j+1] != 1:
                    dp[i%2][j] = -1
                
                if (dp[i%2][j] != dp[(i-1)%2][j]):
                    same_as_prev_row = False
            
            if same_as_prev_row:
                break
        
        final = []

        for i in range(n):
            if dp[total_seconds%2][i] == 0:
                final.append('.')
            if dp[total_seconds%2][i] == 1:
                final.append('L')
            if dp[total_seconds%2][i] == -1:
                final.append('R')
        # 分隔符“” 把char array join成string
        return ''.join(final)
        
