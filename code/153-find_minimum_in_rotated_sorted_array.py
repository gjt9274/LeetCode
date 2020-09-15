class Solution:
    def findMin(self, nums: List[int]) -> int:
        target = nums[-1]
        left, right = 0, len(nums)-2
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                left = mid + 1
            elif nums[mid] < target:
                right = mid - 1
        return nums[left]
