class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return -1
        leftSum = 0
        rightSum = sum(nums) - nums[0]
        index = 0
        while leftSum != rightSum and index < len(nums)-1:
            index += 1
            leftSum += nums[index-1]
            rightSum -= nums[index]

        if leftSum == rightSum:
            return index
        else:
            return -1
