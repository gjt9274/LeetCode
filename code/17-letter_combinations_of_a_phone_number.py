class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        letters = ["", "", "abc", "def", "ghi",
                   "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def backtrack(digits, index, path):
            # 终止条件
            if index == len(digits):
                res.append(path)
                return
            # 选择循环列表
            letter = letters[int(digits[index])]
            for ch in letter:
                # 做出选择
                path = path + ch
                # 递归
                backtrack(digits, index+1, path)
                # 回溯
                path = path[:-1]

        backtrack(digits, 0, "")
        return res
