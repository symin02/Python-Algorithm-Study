# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cnt = 0

        # 경로 중 가장 큰 값을 재귀 함수 매개변수에 포함
        def dfs(root, max_num):
            nonlocal cnt

            if root is None: 
                return
            
            # 현재 노드가 경로의 노드들 중 가장 큰 노드의 값보다 클 경우
            # max_num 갱신 및 cnt + 1
            if root.val >= max_num:
                cnt += 1
                max_num = root.val
            
            # 순서 상관x, 왼쪽 루트부터 탐색함
            dfs(root.left, max_num)
            dfs(root.right, max_num)
        
        dfs(root, root.val)

        return cnt