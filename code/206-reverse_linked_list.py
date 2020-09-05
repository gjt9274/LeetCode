# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#迭代法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev

#递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(cur, prev):
            if not cur:
                return prev
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            return helper(cur, prev)
        return helper(head, None)
