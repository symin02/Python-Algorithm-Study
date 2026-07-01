# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # 1. 트리를 순회하며 리프 노드만 배열로 반환하는 함수
        def get_leaves(node):
            # 노드가 비어있으면 탐색을 멈추고 빈 리스트 반환
            if not node:
                return []
            
            # 리프 노드 조건: 왼쪽 자식과 오른쪽 자식이 모두 없는 경우
            if not node.left and not node.right:
                return [node.val]
            
            # 리프 노드가 아니라면 더 깊이 들어감 (왼쪽 끝까지 갔다가 오른쪽으로)
            # 재귀 호출을 통해 얻은 두 리스트를 하나로 합침(+)
            return get_leaves(node.left) + get_leaves(node.right)
            
        # 2. 두 트리의 리프 노드 배열이 완벽히 똑같은지 비교
        return get_leaves(root1) == get_leaves(root2)