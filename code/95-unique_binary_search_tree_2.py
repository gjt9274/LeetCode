# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#递归
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        ans = []
        if n==0:
            return ans

        return self.helper(1,n)
    
    def helper(self,start,end):
        ans = []
        if start > end:
            ans.append(None)
            return ans
        if start == end:
            root = TreeNode(start)
            ans.append(root)
        
        for i in range(start,end+1): #以每个数为根节点，
            leftTrees = self.helper(start,i-1)  #计算其所有可能的左子树
            rightTrees = self.helper(i+1,end)   #计算其所有可能的右子树

            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    root = TreeNode(i)        
                    root.left = leftTree          #将所有左子树添加为左节点
                    root.right = rightTree        #将所有右子树添加为右节点
                    ans.append(root)
        
        return ans

# 动态规划
# 新增一个大的数，即在原来的树基础上添加，要么添加为根节点，要么是右子结点


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        pre = []
        if n == 0:
            return pre

        pre.append(None)

        #每次增加一个数字
        for i in range(1, n+1):
            cur = []  # 用来保存插入当前数字之后的结果
            for node in pre:
                #c插入为根节点
                cur_node = TreeNode(i)
                cur_node.left = node
                cur.append(cur_node)
                #插入到右孩子,最多找n次右孩子
                for j in range(n):
                    node_copy = self.copyTree(node)
                    #寻找插入右节点的位置
                    right = node_copy
                    k = 0
                    while k < j:
                        if not right:
                            break
                        right = right.right
                        k += 1

                    if not right:
                        break
                    rightTree = right.right
                    cur_node = TreeNode(i)
                    right.right = cur_node  # 插入当前结点为右孩子
                    cur_node.left = rightTree  # 更新原左孩子为插入结点的左孩子

                    cur.append(node_copy)
            pre = cur
        return pre

    def copyTree(self, root):
        if not root:
            return root
        newNode = TreeNode(root.val)
        newNode.left = self.copyTree(root.left)
        newNode.right = self.copyTree(root.right)

        return newNode
