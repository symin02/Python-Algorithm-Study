from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def recur(cur, max_val):
            nonlocal cnt

            if cur is None:
                return

            if cur.val >= max_val:
                cnt += 1
                max_val = cur.val

            recur(cur.left, max_val)
            recur(cur.right, max_val)

        recur(root, root.val)
        return cnt