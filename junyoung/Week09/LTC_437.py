# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cnt = 0
        def dfs(node, node_sum):
            if not node:
                return
            
            node_sum += node.val

            if node_sum == targetSum:
                self.cnt += 1

            dfs(node.left, node_sum)
            dfs(node.right, node_sum)

        # 이진 트리의 모든 노드들을 루트 노드로 dfs 탐색
        def selectAllNodes(node):
            if not node:
                return
            
            dfs(node, 0)
            selectAllNodes(node.left)
            selectAllNodes(node.right)
        
        selectAllNodes(root)

        return self.cnt
        