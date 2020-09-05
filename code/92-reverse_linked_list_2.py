# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head

        dummpy_node = ListNode(0)
        dummpy_node.next = head

        #[3,5]
        cur = dummpy_node
        begin = dummpy_node
        # 遍历到m
        i = 0
        while i < m:
            begin = cur
            cur = cur.next
            i += 1
        # 遍历完之后
        # begin : 3
        # cur: 5
        j = i
        mid = cur  # 5 保存中间那个节点，用于拼接
        prev = None
        while cur and j <= n:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            j += 1
        # 反转完之后
        # prev: 5
        # cur: None
        begin.next = prev
        mid.next = cur
        return dummpy_node.next
