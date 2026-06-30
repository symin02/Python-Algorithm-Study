from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 각 트리의 leaf node를 저장하는 리스트
        root1_leaf = []
        root2_leaf = []

        def dfs(node, arr):
            # 현재 노드 없으면 종료
            if not node:
                return

            # 자식이 모두 없으면 leaf node이므로 값 저장
            if not node.left and not node.right:
                arr.append(node.val)
                return
            
            # 왼쪽과 오른쪽 서브트리 탐색
            dfs(node.left, arr)
            dfs(node.right, arr)

        
        dfs(root1, root1_leaf)
        dfs(root2, root2_leaf)

        # 두 리프노드 순서가 같은지 비교
        return root1_leaf == root2_leaf
        