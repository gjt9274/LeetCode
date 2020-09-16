class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            #时间复杂度变成了 O(n)
            while left < right and nums[left] == nums[left+1]: #去除重复元素
                left += 1
            while right > left and nums[right] == nums[right-1]:
                right -= 1

            mid = left + (right-left) // 2
            if nums[mid] == target:
                return True

            if nums[left] <= nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
