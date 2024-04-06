# https://leetcode.com/problems/distinct-subsequences-ii/description/

# Given a string S, count the number of distinct, non-empty subsequences of S .
# Since the result may be large, return the answer modulo 10^9 + 7.

# S contains only lowercase letters.
# 1 <= S.length <= 2000

# 1. 用dp. dp[i] -- for the first i characters, all the distinct, non-empty subsequences
#    dp[i] = for each string of dp[i-1], append S[i-1] to it, if the string doesn't exists in the dp[i-1] yet
#    abc --> a, b, ab, c, ac, bc, abc
#    but it times out
class Solution:
    """
    @param S: The string s
    @return: The number of distinct, non-empty subsequences of S.
    """
    # dp[i] -- for the first i characters, how many distinct, non-empty subsequences
    # dp[i] = for each string of dp[i-1], append S[i-1] to it, if the string doesn't exists in the dp[i-1] yet
    # 但是这个超时了，主要每个位置都要计算所有情况
    # O(2^N)
    def distinctSubseqII(self, S):

        MOD = 10**9 + 7

        dp = {}
        dp[0]=[]
        dp[1]=[S[0]]

        for i in range(2, len(S) + 1):
            dp[i] = []
            
            if (S[i-1] not in dp[i-1]):
                dp[i].append(S[i-1])
            for sub_sequence in dp[i-1]:
                dp[i].append(sub_sequence)
                new_sequence = "".join([sub_sequence, S[i-1]])
                if new_sequence not in dp[i-1]:
                    dp[i].append(new_sequence)

        return len(dp[len(S)])%MOD

# 1. 用dp. dp[i] -- 以S[i-1]为结尾的 all the distinct, non-empty subsequences
#    dp[i] = 假如S[i-1]存在过 那么从之前的地方往后加所有情况 = dp[prev + 1] + dp[1] + ... + dp[i-1]
#            假如没有存在过，那么从dp[0]开始加
#    dp[0] = 1 ---> 以空字符结尾为1，这样可以在其之后假如当前字符本身
#    O（N^2）
class Solution:
    """
    @param S: The string s
    @return: The number of distinct, non-empty subsequences of S.
    """
    def distinctSubseqII(self, S):
        MOD = 10**9 + 7

        char_position = {}

        dp = [0 for i in range(len(S) + 1)]

        dp[0] = 1

        for i in range(1, len(S) + 1):
            # 如果之前没有这个char的话
            if (S[i-1] not in char_position):
                for j in range(0, i):
                    # 在把这个char加到之前每个结果后面
                    dp[i] += dp[j]
            # 如果有这个char了
            # 那么之前一样的char 已经作为ending 字符计算过一次
            # 就不必再找之前的char之前的了
            # 就从之前那个char开始找
            else:
                prevIndex = char_position[S[i-1]]
                for j in range(prevIndex + 1, i):
                    dp[i] += dp[j]
            
            # 更新最新的位置
            char_position[S[i-1]] = i - 1

        result = 0

        for i in range(1, len(S) + 1):
            print(dp[i])
            result += dp[i]

        result %= MOD
        
        return result
