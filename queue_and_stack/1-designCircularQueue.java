class MyCircularQueue {
    public int head = 0;
    public int count = 0;
    public int capacity;
    public int[] arr;

    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        capacity = k;
        arr = new int[k];
    }

    /**
     * Insert an element into the circular queue. Return true if the operation is
     * successful.
     */
    public boolean enQueue(int value) {
        if (!isFull()) {
            arr[(head + count) % capacity] = value;
            count++;
            return true;
        }
        return false;
    }

    /**
     * Delete an element from the circular queue. Return true if the operation is
     * successful.
     */
    public boolean deQueue() {
        if (!isEmpty()) {
            head = (head + 1) % capacity;
            count--;
            return true;
        }
        return false;
    }

    /** Get the front item from the queue. */
    public int Front() {
        if (isEmpty()) {
            return -1;
        }
        return arr[head];
    }

    /** Get the last item from the queue. */
    public int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return arr[(head + count - 1) % capacity];
    }

    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        return count == 0;
    }

    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return count == capacity;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k); boolean param_1 =
 * obj.enQueue(value); boolean param_2 = obj.deQueue(); int param_3 =
 * obj.Front(); int param_4 = obj.Rear(); boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */