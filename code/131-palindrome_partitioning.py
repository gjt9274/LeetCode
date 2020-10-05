class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [[s]]

        res = []

        def checkPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(path, start):
            # 终止条件
            if start == len(s):
                res.append(path)
                return

            # 选择列表
            for i in range(start, len(s)):
                # 剪枝
                # 判断前缀是否是回文串，否则剪枝
                if not checkPalindrome(start, i):
                    continue
                # 做出选择
                path = path + [s[start:i+1]]
                # 递归
                backtrack(path, i+1)
                # 回溯
                path = path[:-1]
        backtrack([], 0)
        return res
