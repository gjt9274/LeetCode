class Solution:
    def jump(self, nums: List[int]) -> int:
        start = 0  # 第一次起跳开始位置
        end = 1  # 第一次起跳结束位置
        max_i = 0
        ans = 0
        while end < len(nums):
            for i in range(start, end):
                max_i = max(max_i, i+nums[i])
            start = end  # 下一次起跳开始位置
            end = max_i + 1  # 下次起跳结束
            ans += 1
        return ans
