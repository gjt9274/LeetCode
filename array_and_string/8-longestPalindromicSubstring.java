class Solution {
    public String longestPalindrome(String s) {
        // 定义状态矩阵，dp[i][j] 表示 s第i个字符到第j个字符之间最长回文子串的长度
        int n = s.length();
        if (n < 2) {
            return s;
        }
        boolean[][] dp = new boolean[n][n];

        int maxLen = 1;
        int begin = 0;

        // 初始化, dp[i][i] = 1
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }

        // 状态转移方程
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) != s.charAt(j)) {
                    dp[i][j] = false;
                } else {
                    if (j - i + 1 < 4) {
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1];
                    }
                }
                if (dp[i][j] && j - i + 1 > maxLen) {
                    maxLen = j - i + 1;
                    begin = i;
                }
            }
        }

        return s.substring(begin, begin + maxLen);

    }
}