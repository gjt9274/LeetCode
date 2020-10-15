class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int minLen = nums.length + 1;
        int sumNum = 0;
        int left = 0, right = 0;
        while (right < nums.length) {
            sumNum += nums[right];
            right += 1;
            while (sumNum >= s) { // 判断条件，缩小窗口
                if (right - left - 1 < minLen) {
                    minLen = right - left;
                }
                sumNum -= nums[left];
                left++;
            }
        }
        return minLen == nums.length + 1 ? 0 : minLen;
    }
}