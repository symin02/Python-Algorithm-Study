# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        def dfs(root, isLeft, cnt):
            if root is None:
                return
            
            self.max_sum = max(self.max_sum, cnt)
            
            # 전의 방향이 왼쪽이라면
            if isLeft:
                # 왼쪽으로 가면 지그재그 조건이 아니므로 cnt 1로 초기화
                dfs(root.left, True, 1)
                # 오른쪽으로 가면 지그재그 조건 충족하므로 cnt + 1
                dfs(root.right, False, cnt + 1)

            # 전의 방향이 오른쪽이라면
            else:
                dfs(root.left, True, cnt + 1)
                dfs(root.right, False, 1)
            
        
        # 왼쪽
        dfs(root, True, 0)

        # 오른쪽
        dfs(root, False, 0)

        return self.max_sum

