# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            n = len(queue)
            tmp = []
            for i in range(n):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                  queue.append(node.left)
                if node.right:
                  queue.append(node.right)

            res.append(tmp)

        return res[::-1]
