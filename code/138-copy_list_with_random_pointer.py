"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 使用hashMap
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        nodeMap = {}
        cur = head
        while cur:
            nodeMap[cur] = Node(cur.val, None, None)  # 不用赋值next结点，因为map中还没有
            cur = cur.next

        #在遍历一次，复制next和random指针
        cur = head
        while cur:
            clone = nodeMap.get(cur)
            clone.next = nodeMap.get(cur.next)
            clone.random = nodeMap.get(cur.random)
            cur = cur.next

        return nodeMap.get(head)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #1. 复制节点，紧挨到后面
        if not head:
            return head
        cur = head
        while cur:
            clone = Node(cur.val,cur.next,None)
            tmp = cur.next #保存下一个结点
            cur.next = clone #复制节点到后面
            cur = tmp

        # 2. 处理随机指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 4. 分离两个链表
        cur = head
        copy = head.next
        while cur and cur.next:
            tmp = cur.next
            cur.next = cur.next.next
            cur = tmp
        
        return copy
