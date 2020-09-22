# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        firstNode = head    #前一个结点
        nextNode = head.next  #后一个结点
        firstNode.next = self.swapPairs(nextNode.next)  # 递归的输入为后一个结点的next指针，递归的返回值为后一个结点
        nextNode.next = firstNode     #更新后一个结点的next指针指向前一个结点

        return nextNode
