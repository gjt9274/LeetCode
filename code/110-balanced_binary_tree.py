# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def find_depth(root):
            depth = 1
            if not root:
                return 0
            left_depth = find_depth(root.left)
            right_depth = find_depth(root.right)
            if left_depth == -1 or right_depth == -1 or left_depth-right_depth > 1 or right_depth-left_depth > 1:
                return -1
            depth += left_depth if left_depth > right_depth else right_depth
            return depth

        res = find_depth(root)
        if res == -1:
            return False
        return True
