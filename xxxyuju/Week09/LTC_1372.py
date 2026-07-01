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

        def zigzag(node, direction, length):
            nonlocal ans
            if not node:
                return

            # 현재까지의 지그재그 길이 갱신
            ans = max(ans, length)

            if direction == 'L':
                # 이전에 왼쪽으로 왔다면 다음은 오른쪽으로 가야 길이 증가
                zigzag(node.right, 'R', length+1)

                # 같은 방향인 왼쪽으로 가는 경우 경로 다시 시작
                zigzag(node.left, 'L', 1)
            else:
                # 오른쪽으로 온 경우도 마찬가지
                zigzag(node.left, 'L', length+1)
                zigzag(node.right, 'R', 1)

        zigzag(root.left, 'L', 1)
        zigzag(root.right, 'R', 1)

        return ans