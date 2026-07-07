# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return None

            # 현재 노드가 p 또는 q라면 찾은 것이므로 return
            if node == p or node == q:
                return node

            # 왼쪽과 오른쪽 서브트리 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 양쪽 모두 값이 있으면 현재 노드가 LCA
            if left and right:
                return node
            
            # 한쪽에서만 찾은 경우
            return left if left else right
        
        return dfs(root)