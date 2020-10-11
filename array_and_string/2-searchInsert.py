class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            medium = left + (right - left) // 2
            if (nums[medium] == target):
                return medium
            elif target < nums[medium]:
                right = medium
            elif target > nums[medium]:
                left = medium+1
            
        return left
    
