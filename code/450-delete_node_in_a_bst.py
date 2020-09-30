# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # 三种情况
            # 1. 被删除结点没有左子树，则返回其右子树
            if not root.left:
                return root.right
            elif not root.right:  # 2. 被删除结点没有右子树，则返回其左子树
                return root.left
            else:  # 左右子树都有，则将左子树添加到右子树的最左子节点
                node = TreeNode()
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                return root.right
        return root
