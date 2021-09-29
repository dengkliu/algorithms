# https://www.lintcode.com/problem/512/

# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Input: "12"
# Output: 2
# Explanation: It could be decoded as AB (1 2) or L (12).

# dp[i] -- 前i个数有多少种方法
# dp[i] = 假如i是0的话，只能和前一个数合并，而且前一个数只能是0或者 否则不存在方法 dp[i-2]
#       = 假如是1-9的话，可以独立成一个字母，dp[i-1], 或者假如和前一个数合起来是11到26之间的话 dp[i-2]
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        characters = list(s)
        n = len(characters)

        if not s or n == 0:
            return 0

        dp = [0 for _ in range(n + 1)]

        dp[0] = 1

        if(characters[0] == '0'):
            return 0
        
        dp[1] = 1

        for i in range(2, n + 1):
            
            # 0 只能和之前的数组合并
            if characters[i-1] == '0':
                if characters[i-2] == '1' or characters[i-2] == '2':
                    dp[i] = dp[i-2]
                    continue
                else:
                    return 0
            
            # 不是0的话，可以自己分出来decode
            dp[i] = dp[i-1]

            # 或者前面的合并decode,从11到26
            if characters[i-2] == '1': 
                dp[i] += dp[i-2]
            elif characters[i-2] == '2' and int(characters[i-1]) <= 6:
                dp[i] += dp[i-2]
        
        return dp[n]