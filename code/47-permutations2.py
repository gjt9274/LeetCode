class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        visited = {index: False for index in range(len(nums))}

        def backtrack(nums, path, visited):
            # 终止条件
            if len(path) == len(nums):
                res.append(path)
                return
            # 做出选择
            for i in range(len(nums)):
                # 剪枝
                # 1. 如果被访问过
                if visited[i]:
                    continue
                # 2. 如果前一个数没被访问且后一个数等于前一个数
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                # 做出选择
                path = path + [nums[i]]
                visited[i] = True
                # 递归
                backtrack(nums, path, visited)
                # 回溯
                visited[i] = False
                path = path[:-1]
        backtrack(nums, [], visited)
        return res

if __name__ == "__main__":
    s = Solution()
    res =s.permuteUnique([1,1,2])