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
