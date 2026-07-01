from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0

        def dfs(node, arr):
            nonlocal cnt

            if not node:
                return 0

            new_arr = []

            # 이전 경로 합들에 현재 노드 값을 더함
            for x in arr:
                new_arr.append(x + node.val)

            # 현재 노드에서 새로 시작하는 경로 추가
            new_arr.append(node.val)


            # 현재 노드를 포함한 경로 중 targetSum과 같은 경우 카운트
            for s in new_arr:
                if s == targetSum:
                    cnt += 1
                    
            dfs(node.left, new_arr)
            dfs(node.right, new_arr)

            

        dfs(root, [])
        return cnt