class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心算法，遍历数组，如果当前位置加上当前可以跳的步数，
        # 能到达的最远，可以超过数组长，说明可以到达
        max_i = 0
        for i, jump in enumerate(nums):
            if i > max_i:   #说明后面的位置都不可以到达
                return False
            max_i = max(max_i, i+jump)
        return True


