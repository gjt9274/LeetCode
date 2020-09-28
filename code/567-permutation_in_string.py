from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        s1_lookup = {chr(i): 0 for i in range(97, 123)}
        s2_lookup = {chr(i): 0 for i in range(97, 123)}

        for i in range(n1):
            s1_lookup[s1[i]] += 1
            s2_lookup[s2[i]] += 1

        for i in range(n2-n1):
            if s1_lookup == s2_lookup:
                return True
            s2_lookup[s2[i+n1]] += 1  #固定的窗口大小
            s2_lookup[s2[i]] -= 1

        return s1_lookup == s2_lookup


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        target_dict = defaultdict(lambda: 0)
        window_dict = defaultdict(lambda: 0)

        for i in range(n1):
            target_dict[s1[i]] += 1

        left, right = 0, 0
        distance = 0

        while right < n2:
            ch = s2[right]
            right += 1
            if target_dict[ch] != 0:  # 字符存在目标子串中
                window_dict[ch] += 1
                if window_dict[ch] == target_dict[ch]:
                    distance += 1

            while right - left >= n1:  # 当窗口长度大于目标子串长度，开始缩紧窗口
                if distance == len(set(s1)):  # 注意：是等于目标串的字符种类数
                    return True
                ch_rmv = s2[left]  # 需要移除的左端字符
                left += 1
                if target_dict[ch_rmv] != 0:
                    if window_dict[ch_rmv] == target_dict[ch_rmv]:
                        distance -= 1

                    window_dict[ch_rmv] -= 1

        return False

