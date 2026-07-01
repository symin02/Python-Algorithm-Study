# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
    
        # 현재 노드와 지금까지 지나온 경로의 최댓값을 같이 받음
        def dfs(node, max_val):
            # 빈 공간에 도달하면 0을 리턴
            if not node:
                return 0
            
            # 내 값이 지금까지의 최댓값보다 >= 1점 획득, 아니면 0점
            count = 1 if node.val >= max_val else 0
            
            # 새로운 최댓값 갱신
            new_max = max(max_val, node.val)
            
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            
            return count

        return dfs(root, root.val)