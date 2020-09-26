class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        minLen = len(nums) + 1
        left, right = 0, 0
        sumNum = 0
        while right < len(nums):
            sumNum += nums[right]
            right += 1
            while sumNum >= s:
                minLen = min(minLen, right-left)
                sumNum -= nums[left]
                left += 1

        return 0 if minLen == len(nums) + 1 else minLen
