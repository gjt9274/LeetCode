class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) {
            return 0;
        }
        int n = haystack.length(), m = needle.length();
        // 定义 next 数组
        int[] next = new int[m];
        // 初始化 next 数组
        initNext(next, needle);
        // 匹配
        int j = -1;
        for (int i = 0; i < n; i++) {
            while (j >= 0 && haystack.charAt(i) != needle.charAt(j + 1)) {
                j = next[j]; // 寻找之前匹配的位置
            }
            if (haystack.charAt(i) == needle.charAt(j + 1)) {
                // 如果匹配，则i,j 同时向后移动
                j++;
            }
            if (j == needle.length() - 1) {
                return i - needle.length() + 1; // 文本串中出现模式串
            }
        }

        return -1;
    }

    public void initNext(int[] next, String s) {
        int j = -1;
        next[0] = j;
        for (int i = 1; i < s.length(); i++) { // 注意 i 从 1 开始
            while (j >= 0 && s.charAt(i) != s.charAt(j + 1)) { // 前后缀不相同了
                j = next[j]; // 向前回溯
            }
            if (s.charAt(i) == s.charAt(j + 1)) { // 找到相同的前后缀
                j++;
            }
            next[i] = j; // 将 j （前缀长度） 赋给 next[i]
        }
    }
}