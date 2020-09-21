class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # 定义状态
        dp = [False] * (n+1)  # dp[i]表示s的前i个单词是否可以合理切分为单词

        # 初始化
        dp[0] = True  # dp[0]表示空字符，可以正确组成单词

        # 状态转移
        for i in range(1, n+1):
            for j in range(0, i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break

        return dp[n]
