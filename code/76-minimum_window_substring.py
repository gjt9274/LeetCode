from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ""
        # 使用defaultdict可以为不存在的key提供默认值，表面KeyError
        t_freq = defaultdict(lambda: 0)  # 用来表示子串中字符的频数表
        win_freq = defaultdict(lambda: 0)  # 用来表示滑动窗口内字符的频数表

        for i in t:
            t_freq[i] += 1

        min_len = len(s) + 1  # 最小覆盖子串的长度
        begin = 0  # 最小覆盖子串的起始下标

        left, right = 0, 0  # 华东窗口的左右指针
        distance = 0  # 用来表示滑动窗口是否覆盖了目标子串

        while right < len(s):
            if t_freq[s[right]] == 0:
                right += 1
                continue

            if win_freq[s[right]] < t_freq[s[right]]:  # 当向右滑动，出现了目标子串中出现的字符，且窗口内的字符个数小于目标子串
                distance += 1
            win_freq[s[right]] += 1
            right += 1

            while distance == len(t):  # 当覆盖了目标子串
                if right - left < min_len:
                    min_len = right - left
                    begin = left
                if t_freq[s[left]] == 0:
                    left += 1
                    continue
                if win_freq[s[left]] == t_freq[s[left]]:
                    distance -= 1

                win_freq[s[left]] -= 1
                left += 1
        if min_len == len(s) + 1:
            return ""
        return s[begin:begin+min_len]
