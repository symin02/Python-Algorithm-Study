from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 현재 노드가 없으면 depth는 0
        if not root:
            return 0

        # 왼쪽 서브트리와 오른쪽 서브트리의 depth를 재귀로 계산
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # 두 서브트리 중 더 깊은 쪽에 현재 노드의 depth 1을 더해 반환
        return max(left, right) + 1