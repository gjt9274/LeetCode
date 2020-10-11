class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        win_dict = defaultdict(lambda: 0)
        left, right, maxLen = 0, 0, 0
        while left < len(s):
            while right < len(s) and win_dict[s[right]] == 0:
                win_dict[s[right]] = 1
                right += 1
            # if right == len(s):
            #     return right - left
            if right - left > maxLen:
                maxLen = right - left
            left += 1
            right = left
            win_dict.clear()

        return maxLen


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        lookup = set()
        maxLen = 0
        right = -1
        for left in range(len(s)):
            if left != 0:
                lookup.remove(s[left-1])  #移除左边元素
            while right+1 < len(s) and s[right+1] not in lookup: #[left+1,right]一定没有重复元素，所以继续移动右指针
                lookup.add(s[right+1])
                right += 1
            maxLen = max(maxLen, right-left + 1)

        return maxLen


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        ans = 0
        win = defaultdict(lambda: 0)
        while right < len(s):
            c = s[right]
            win[c] += 1
            right += 1
            while win[c] > 1:  # 缩小窗口
                d = s[left]
                left += 1
                win[d] -= 1
            ans = max(ans, right-left)

        return ans
