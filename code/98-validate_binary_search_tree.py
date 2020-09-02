# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#利用中序遍历的结果，如果是有序的，则表明是二叉搜索树
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []

        def inOrder(root):
            if not root:
                return []

            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

            return res

        res = inOrder(root)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        return True
