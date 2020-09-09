class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st = []
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.queue:
            self.st.append(self.queue.pop())
        self.queue.append(x)
        while self.st:
            self.queue.append(self.st.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.queue:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
