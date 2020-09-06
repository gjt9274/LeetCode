# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        # 从中间断开，将后面反转，然后看两个链表是否相等
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = slow.next
        slow.next = None
        tail = self.reverseList(tail)
        while tail and head:
            if tail.val != head.val:  # 判断值
                return False
            tail = tail.next
            head = head.next
        return True

    def reverseList(self, head):
        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
