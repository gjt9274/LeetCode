class Solution {
    public void moveZeroes(int[] nums) {
        int len = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[len++] = nums[i];
            }
        }
        while (len < nums.length) {
            nums[len++] = 0;

        }
    }
}