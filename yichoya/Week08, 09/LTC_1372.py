from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def recur(cur, prev_dir, length):
            nonlocal ans

            if cur is None:
                return

            ans = max(ans, length)

            # left = 1, right = 0
            if prev_dir == 1:
                recur(cur.right, 0, length + 1)
                recur(cur.left, 1, 1)
            else:
                recur(cur.left, 1, length + 1)
                recur(cur.right, 0, 1)

        recur(root.left, 1, 1)
        recur(root.right, 0, 1)

        return ans