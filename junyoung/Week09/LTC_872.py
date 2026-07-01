# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(cur, arr):
            if cur is None:
                return

            # 왼쪽, 오른쪽 자식 노드가 없을 때 -> 리프 노드
            if cur.left == None and cur.right == None:
                arr.append(cur.val)
                return 
            # 왼쪽 노드부터 우선 탐색
            dfs(cur.left, arr)
            dfs(cur.right, arr)           
        
        arr1 = []
        arr2 = []

        dfs(root1, arr1)
        dfs(root2, arr2)

        return arr1 == arr2