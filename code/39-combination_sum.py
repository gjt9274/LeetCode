class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(candidates, tmp, sumTemp, start, target):
            # 终止条件
            if sumTemp == target:
                res.append(tmp)
                return
            # 选择列表
            for i in range(start, len(candidates)):
                # 剪枝
                if sumTemp > target:
                    continue
                # 做出选择
                tmp = tmp + [candidates[i]]
                # 递归下一层
                backtrack(candidates, tmp, sumTemp+candidates[i], i, target)
                # 回溯
                tmp = tmp[:-1]
        backtrack(candidates, [], 0, 0, target)
        return res
