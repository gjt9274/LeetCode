class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxLen = 0, slow = -1, fast = 0;
        for (; fast < nums.length; fast++) {
            if (nums[fast] != 1) {
                maxLen = (fast - slow > maxLen) ? fast - slow - 1 : maxLen;
                slow = fast;
            }
        }
        return (fast - slow > maxLen) ? fast - slow - 1 : maxLen;

    }
}