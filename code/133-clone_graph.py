"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #建立一个哈希表用于保存已经访问过的结点
        # visited = {}
        # def cloneDFS(node,visited):
        #     if not node:
        #         return None
        #     if node in visited:
        #         return visited[node]

        #     cloneNode = Node(node.val)
        #     visited[node] = cloneNode
        #     for n in node.neighbors:
        #         cloneNode.neighbors.append(cloneDFS(n,visited))
        #     return cloneNode
        # return cloneDFS(node,visited)
        visited = {}

        def cloneBFS(node, visited):
            if not node:
                return None
            q = []
            clone = Node(node.val)
            q.append(node)
            visited[node] = clone
            while len(q) != 0:
                cur = q.pop(0)
                for n in cur.neighbors:
                    if n not in visited:
                        visited[n] = Node(n.val)
                        q.append(n)
                    visited[cur].neighbors.append(visited[n])
            return clone
        return cloneBFS(node, visited)
