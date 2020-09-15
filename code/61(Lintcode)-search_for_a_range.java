public class Solution {
    /**
     * @param A: an integer sorted array
     * @param target: an integer to be inserted
     * @return: a list of length 2, [index1, index2]
     */
    public int[] searchRange(int[] A, int target) {
        // write your code here
        if (A.length == 0) return new int[]{-1,-1};
        int left = searchLeftPosition(A,target);
        int right = searchRightPosition(A,target);
        return new int[]{left,right};
    }
    //找左端点
    public int searchLeftPosition(int[] A, int target){
        int left = 0;
        int right = A.length- 1;
        while (left <= right){
            int mid = left + (right-left) / 2;
            if (A[mid] == target){
                right = mid-1;
            }else if (A[mid] < target){
                left = mid + 1;
            } else if(A[mid] > target){
                right = mid - 1;
            }
        }
        if (left >= A.length || A[left] != target){
            return -1;
        }
        return left;
    }
    //找右端点
    public int searchRightPosition(int[] A, int target){
        int left = 0;
        int right = A.length - 1;
        while (left <= right){
            int mid = left + (right-left) / 2;
            if (A[mid] == target){
                left = mid+1;
            }else if (A[mid] < target){
                left = mid + 1;
            } else if(A[mid] > target){
                right = mid - 1;
            }
        }
        if (right < 0 || A[right] != target){
            return -1;
        }
        return right;
    }
}