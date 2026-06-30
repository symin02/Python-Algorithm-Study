from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good node의 개수
        cnt = 0
        
        def dfs(node, x):
            nonlocal cnt
            
            if not node:
                return 0

            # 현재 노드 값이 경로의 최댓값 이상이면 good node
            if x <= node.val:
                cnt += 1

            # 최댓값을 갱신하며 자식 노드 탐색
            dfs(node.left, max(x, node.val))
            dfs(node.right, max(x, node.val))

            
        dfs(root, root.val)
        return cnt