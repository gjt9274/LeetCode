import java.util.Deque;

class Solution{
    public int[] dailyTemperatures(int[] T){
        Deque<Integer> stack = new LinkedList<>();
        int[] ans = new int[T.length];
        for(int i = 0; i < T.length; i++){
            int curT = T[i];;
            while(!stack.isEmpty() && curT > T[stack.peek()]){
                int prevIndex = stack.pop();
                ans[prevIndex] = i - prevIndex;
            }
            stack.push(i);
        }
        return ans;
    }
}