class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # 누적 합의 빈도를 저장하는 딕셔너리 (해시맵)
        # 초기값 {0: 1}은 '루트 노드부터 시작하는 경로'가 바로 정답이 될 때를 처리하기 위함입니다.
        prefix_map = {0: 1}
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # 1. 현재 노드 값을 더해 누적 합 갱신
            current_sum += node.val
            
            # 2. (현재 누적 합 - targetSum)이 해시맵에 있는지 확인
            # 존재한다면, 그 빈도수만큼 targetSum을 만족하는 경로가 있다는 뜻
            target = current_sum - targetSum
            count = prefix_map.get(target, 0)
            
            # 3. 현재 누적 합을 해시맵에 기록 (방문 처리)
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
            
            # 4. 왼쪽, 오른쪽 자식 노드로 DFS 탐색을 이어나감
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # 5. 백트래킹 (Backtracking)
            # 이 노드에서의 탐색이 끝났으므로, 다른 갈래(Branch)에 영향을 주지 않도록 
            # 현재 누적 합의 빈도를 1 줄여줍니다.
            prefix_map[current_sum] -= 1
            
            return count
        
        return dfs(root, 0)