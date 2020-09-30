class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = {num: False for num in nums}

        def backtrack(nums, path, visited):
            # 终止条件
            if len(path) == len(nums):
                res.append(path)
                return
            # 选择列表
            for num in nums:
                # 剪枝，如果元素已经访问过，则继续
                if visited[num]:
                    continue
                # 做出选择
                path = path + [num]
                visited[num] = True # 设置元素已经访问
                # 递归
                backtrack(nums, path, visited)
                # 回溯
                visited[num] = False # 重新设为未访问
                path = path[:-1]

        backtrack(nums, [], visited)
        return res
