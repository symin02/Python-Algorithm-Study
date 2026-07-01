from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def recur(cur, li):
            # 탈출조건
            if cur is None:
                return

            # 현재 노드가 리프노드라면 return
            if cur.left == None and cur.right == None:
                li.append(cur.val)
                return

            recur(cur.left, li)
            recur(cur.right, li)

        # root1, root2 순회하면서 리프노드 값을 추가할 배열
        leaves1 = []
        leaves2 = []
        recur(root1, leaves1)
        recur(root2, leaves2)
        return leaves1 == leaves2