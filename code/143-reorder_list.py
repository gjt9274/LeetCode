# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 思路
        # 找到中断的点，将链表分成两段（快慢指针）
        # 反转后面那段，然后合并两个链表
        if not head:
            return head

        #找到中断点
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = slow.next
        slow.next = None  # 断开
        #反转后半段
        tail = self.reverse(tail)
        #合并两端
        head = self.mergeTwoList(head, tail)
        return head

    def reverse(self, head: ListNode):
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev

    def mergeTwoList(self, l1: ListNode, l2: ListNode):
        dummy_node = ListNode(0)
        cur = dummy_node
        toggle = True

        while l1 and l2:
            if toggle:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            toggle = not toggle  # 切换
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return cur
