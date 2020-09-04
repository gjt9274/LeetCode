# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 因为可能删掉头节点，所以需要一个dummpy node
        dummpy_node = ListNode(0)
        dummpy_node.next = head
        cur = dummpy_node
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                rm_val = cur.next.val
                while cur.next and cur.next.val == rm_val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummpy_node.next
