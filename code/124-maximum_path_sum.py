# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = float(-inf)

    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            left_max_path = helper(root.left)
            right_max_path = helper(root.right)

            self.ans = max(self.ans, max(left_max_path, 0) +
                           max(right_max_path, 0) + root.val)
            return max(left_max_path, right_max_path, 0) + root.val
        helper(root)
        return self.ans
