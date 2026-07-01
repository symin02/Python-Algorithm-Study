# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # 트리를 탐색하면서 잎 노드만 리스트에 담아주는 보조 함수를 만듦
        def get_leaves(node, leaves_list):
            if not node:
                return  # 빈 공간이면 그냥 돌아감
            
            # 왼/오 모두 없으면 Leaf 노드임
            if not node.left and not node.right:
                leaves_list.append(node.val)
                
            # 왼쪽을 먼저, 그 다음 오른쪽
            get_leaves(node.left, leaves_list)
            get_leaves(node.right, leaves_list)

        # leaves1, leaves2라는 빈 배열을 선언
        leaves1 = []
        leaves2 = []
        
        # 두 트리의 루트를 각각 보조 함수에 넣어 리프 노드 배열
        get_leaves(root1, leaves1)
        get_leaves(root2, leaves2)
        
        # ==를 사용해 두 배열이 완전히 같은지 판별하여 리턴
        return leaves1 == leaves2