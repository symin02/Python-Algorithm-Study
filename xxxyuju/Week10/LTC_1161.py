from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sums = []
        q = deque()
        q.append((root, 0))

        while q:
            node, depth = q.popleft()

            # 처음 보는 depth면 새로운 sum 공간 만들기
            if depth == len(level_sums):
                level_sums.append(0)

            # 해당 depth의 합에 현재 노드 값 더하기
            level_sums[depth] += node.val

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))


        return level_sums.index(max(level_sums)) + 1
        