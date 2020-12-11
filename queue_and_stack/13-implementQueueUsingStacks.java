class MyQueue {

    public Deque<Integer> temp;
    public Deque<Integer> res;
    /** Initialize your data structure here. */
    public MyQueue() {
        temp = new LinkedList<>();
        res = new LinkedList<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        while(!res.isEmpty()){
            temp.push(res.pop());
        }
        res.push(x);
        while(!temp.isEmpty()){
            res.push(temp.pop());
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        return res.pop();
    }
    
    /** Get the front element. */
    public int peek() {
        return res.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return res.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */