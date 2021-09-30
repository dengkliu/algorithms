# https://www.lintcode.com/problem/676/
# A message containing letters from A-Z is being encoded to numbers using the following mapping way:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Beyond that, now the encoded string can also contain the character *, which can be treated as one of the numbers from 1 to 9.
# Given the encoded message containing digits and the character *, return the total number of ways to decode it.
# Also, since the answer may be very large, you should return the output mod 10^9 + 7.

class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """
    # dp[i] --> for first i numbers, how many ways
    # dp[i] = 假如i是0的话，只能和前一个数合并，而且前一个数只能是0或者1或者* 否则不存在方法 dp[i-2]
    #       = 假如是1-9的话，
    #         1. 可以独立成一个字母，dp[i-1], 
    #         2. 前一个数字是1 -- dp[i-2]
    #         3. 前一个数字是2并且现在这个数字小于7 -- dp[i-2]
    #         4. 前一个数字是* --- 以上两种情况的综合
    #       = 假如是*的话，可以独立成一个字母，dp[i-1]*9, 或者假如前一个字母是1或者*的话，dp[i-2]*9，前一个字母是2的话，dp[i-2]*6
    #         1. 可以独立成一个字母 9*dp[i-1]
    #         2. 前一个数字是1 -- 9*dp[i-2]
    #         3. 前一个数字是2 -- 6*dp[i-2]
    #         4. 前一个数字是* -- 15*dp[i-2]
    def numDecodings(self, s):
        
        MOD = 10**9 + 7

        characters = list(s)
        
        n = len(characters)
            
        if not s or n == 0:
            return 0
            
        dp = [0 for _ in range(n + 1)]

        dp[0] = 1
            
        if(characters[0] == '0'):
            return 0
        elif(characters[0] == '*'):
            dp[1] = 9
        else:
            dp[1] = 1
            
        for i  in range(2, n + 1):
            
            if characters[i-1] == '0':
                if characters[i-2] == '1' or characters[i-2] == '2' or characters[i-2] == '*':
                    dp[i] = dp[i-2]
                    continue
                else:
                    return 0
                
            if characters[i-1] == '*':
                # 单独decode
                dp[i] = 9 * dp[i-1]
                # 和前面一起decode
                if characters[i-2] == '1':
                    dp[i] += dp[i-2]*9
                elif characters[i-2] == '2':
                    dp[i] += dp[i-2]*6
                elif characters[i-2] == '*':
                    dp[i] += dp[i-2]*15
                
            else:
                # 单独decode
                dp[i] = dp[i-1]
                # 和前面一起decode
                if characters[i-2] == '1':
                    dp[i] += dp[i-2]
                elif characters[i-2] == '2' and int(characters[i-1]) <= 6:
                    dp[i] += dp[i-2]
                elif characters[i-2] == '*':
                    if int(characters[i-1]) <= 6 :
                        dp[i] += 2 * dp[i-2]
                    else:
                        dp[i] += dp[i-2]
                    
        return dp[n]%MOD