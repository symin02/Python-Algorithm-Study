# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # 현재 노드가 좋은 노드인지 확인
            count = 1 if node.val >= max_val else 0
            
            # 경로상의 최댓값 갱신
            new_max = max(max_val, node.val)
            
            # 좌우 서브트리 탐색 결과를 합산
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            
            return count

        return dfs(root, root.val)