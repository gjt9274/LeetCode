class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, res = 0, 0, 0
        win_freq = defaultdict(lambda: 0) #表示窗口内个字符出现的次数
        while right < len(s):
            win_freq[s[right]] += 1
            maxCount = max(win_freq.values()) #窗口内出现次数最多的字符的次数
            while right - left+1 - maxCount > k: #窗口长度减去出现次数最多的字符的次数即需要填充的字符的次数
                win_freq[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
            right += 1

        return res
