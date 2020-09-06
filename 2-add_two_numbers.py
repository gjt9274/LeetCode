# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        cur = dummy_node
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            res = l1_val + l2_val + carry
            cur.next = ListNode(res % 10)
            carry = res // 10
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        #最后进1
        if carry == 1:
            cur.next = ListNode(carry)

        return dummy_node.next
