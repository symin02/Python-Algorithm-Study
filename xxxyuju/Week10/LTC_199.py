from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []    # 오른쪽에서 보이는 노드 값을 저장할 리스트
        visited_depth = set()   # 이미 값을 저장한 깊이를 기록하는 set

        def dfs(node, depth):
            if not node:
                return
            
            # 이 깊이를 처음 방문한 경우에만 저장
            if depth not in visited_depth:
                ans.append(node.val)
                visited_depth.add(depth)

            # 오른쪽부터 탐색
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return ans

        