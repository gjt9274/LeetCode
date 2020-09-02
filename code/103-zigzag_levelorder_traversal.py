# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         res = []
#         def inOrder(root):
#             if not root:
#                 return []

#             inOrder(root.left)
#             res.append(root.val)
#             inOrder(root.right)

#             return res


#         res = inOrder(root)
#         for i in range(1,len(res)):
#             if res[i] <= res[i-1]:
#                 return False
#         return True


# 递归
class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, max_val=float('inf'), min_val=float('-inf')):
                if not root:
                    return True
                cur = root.val
                if cur >= max_val or cur <= min_val:  # 如果左子树的最大值大于节点，或者右子树最小值小于节点
                    return False
                if not helper(root.left, cur, min_val):
                    return False
                if not helper(root.right, max_val, cur):
                    return False

                return True
        return helper(root)
