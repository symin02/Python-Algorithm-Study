from collections import deque
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        q = deque([root])
        cnt = 0
        while q:
            # 현재 queue에 있는 같은 레벨의 노드들을 처리
            for _ in range(len(q)):

                cur_node = q.popleft()

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            # 레벨마다 cnt가 증가
            cnt += 1

        return cnt
