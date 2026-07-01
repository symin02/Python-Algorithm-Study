from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0

        # 현재 노드부터 합을 구하는 함수
        def calcSum(cur, total):
            nonlocal ans

            if cur is None:
                return

            total += cur.val

            if total == targetSum:
                ans += 1

            calcSum(cur.left, total)
            calcSum(cur.right, total)

        # 노드 순회 함수
        def nodeCheck(cur):
            if cur is None:
                return

            calcSum(cur, 0)

            nodeCheck(cur.left)
            nodeCheck(cur.right)

        nodeCheck(root)

        return ans