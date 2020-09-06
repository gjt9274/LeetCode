# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            if fast == slow:
                slow = head  # 满指针回到起点
                fast = fast.next  # 快指针从相遇点出发
                while slow != fast:
                    slow = slow.next  # 步伐一致
                    fast = fast.next
                return slow
            slow = slow.next
            fast = fast.next.next

        return None
