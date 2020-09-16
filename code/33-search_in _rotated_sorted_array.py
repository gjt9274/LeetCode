class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  # 左半部分有序
                if nums[mid] >= target and target >= nums[left]:  # 且满足目标值可能在左半部分
                    right = mid - 1
                else:  # 目标值可能在右半部分
                    left = mid + 1
            else:  # 右半部分有序
                if nums[mid] <= target and target <= nums[right]:  # 且满足目标值可能在右半部分
                    left = mid + 1
                else:  # 目标值可能在左半部分
                    right = mid - 1
        return -1
