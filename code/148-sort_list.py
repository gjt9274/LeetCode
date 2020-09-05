# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 思路：
        # 使用归并排序，但是列表不能直接找到中点
        # 需要用快慢指针来找到中点
        def findMiddle(head: ListNode) -> ListNode:
            slow = head
            fast = head.next
            while fast and fast.next:
                fast = fast.next.next  # 步长为2
                slow = slow.next
            return slow

        def mergeList(left: ListNode, right: ListNode) -> ListNode:
            if not left:
                return right
            if not right:
                return left
            dummy_node = ListNode(0)
            cur = dummy_node
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next

            if left:
                cur.next = left
            if right:
                cur.next = right

            return dummy_node.next

        def mergeSort(head: ListNode) -> ListNode:
            if not head or not head.next:
                return head
            middle = findMiddle(head)
            tail = middle.next
            middle.next = None  # 将中间断开
            left = mergeSort(head)
            right = mergeSort(tail)
            res = mergeList(left, right)
            return res

        return mergeSort(head)
