# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        # 왼쪽 노드, 오른쪽 노드의 각각 최대 깊이를 측정(재귀!)
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right) 
        # 양쪽 노드를 비교후 더 깊은 값 고른 후, +1 해서 리턴
        return max(left_depth, right_depth) + 1