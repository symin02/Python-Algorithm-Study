# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        
        # direction: 0 (왼쪽에서 옴), 1 (오른쪽에서 옴)
        def dfs(node, direction, length):
            if not node:
                return
            
            # 매 방문마다 최대 길이 갱신
            self.max_length = max(self.max_length, length)
            
            if direction == 0:  # 이전에 왼쪽으로 내려온 경우
                dfs(node.right, 1, length + 1) # 지그재그 성공 (오른쪽으로)
                dfs(node.left, 0, 1)           # 지그재그 실패 (다시 왼쪽으로)
            else:               # 이전에 오른쪽으로 내려온 경우
                dfs(node.left, 0, length + 1)  # 지그재그 성공 (왼쪽으로)
                dfs(node.right, 1, 1)          # 지그재그 실패 (다시 오른쪽으로)
        
        # 루트 노드에서는 왼쪽으로 가는 경우와 오른쪽으로 가는 경우 둘 다 시작해봄
        # (길이는 0부터 시작)
        dfs(root.left, 0, 1)
        dfs(root.right, 1, 1)
        
        return self.max_length   