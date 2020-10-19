class Solution {
    public int findMin(int[] nums) {
        int len = nums.length;
        int target = nums[len - 1];
        int left = 0, right = len - 2;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > target) {
                left = mid + 1;
            } else if (nums[mid] < target) {
                right = mid - 1;
            }
        }
        return nums[left];
    }
}