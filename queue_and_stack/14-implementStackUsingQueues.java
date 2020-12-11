class MyStack {

    public Queue<Integer> res;
    /** Initialize your data structure here. */
    public MyStack() {
   
        res = new LinkedList<>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        int n = res.size();
        res.add(x);
        for(int i = 0; i < n; i++){
            res.add(res.poll());
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return res.poll();
    }
    
    /** Get the top element. */
    public int top() {
        return res.peek();
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return res.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */