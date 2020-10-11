class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        res = strs[0]
        tmp = ""
        for i in range(1, len(strs)):
            cur = strs[i]
            n = min(len(res), len(cur))
            for j in range(n):
                if j == 0 and res[j] != cur[j]:
                    return ""
                if res[j] == cur[j]:
                    tmp += cur[j]
                else:
                    res = tmp
                    tmp = ""
                    break
            else:
                res = tmp
                tmp = ""
        return res
