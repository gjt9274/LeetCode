class MinStack {
    public Deque<Integer> stack;
    public Deque<Integer> minStack;

    /** initialize your data structure here. */
    public MinStack() {
        stack = new LinkedList<>();
        minStack = new LinkedList<>();
    }

    public void push(int x) {
        if (stack.isEmpty()) {
            minStack.push(x);
        } else {
            int min = minStack.peek();
            if (x < min) {
                minStack.push(x);
            } else {
                minStack.push(min);
            }
        }
        stack.push(x);
    }

    public void pop() {
        stack.pop();
        minStack.pop();
    }

    public int top() {
        int res = stack.peek();
        return res;
    }

    public int getMin() {
        int min = minStack.peek();
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such: MinStack obj =
 * new MinStack(); obj.push(x); obj.pop(); int param_3 = obj.top(); int param_4
 * = obj.getMin();
 */