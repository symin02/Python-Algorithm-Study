# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        # 과거의 누적합을 저장할 딕셔너리 
        # 키: 누적합, 값(value): 해당 누적합이 발생한 횟수
        prefix_sums = defaultdict(int)
        
        #  처음에 아무것도 더하지 않았을 때의 합은 0이므로, 0을 1번 만들었다고 미리 기록
        prefix_sums[0] = 1 
        
        #  탐색 DFS 헬퍼 함수
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # 현재 노드의 값을 더해서 지금까지의 누적합을 구함
            current_sum += node.val
            
            # 내가 찾고 싶은 과거의 누적합은 (현재 누적합 - 목표합)
            # 만약 기록이 존재한다면, 그 횟수만큼 정답 카운트에 +
            count = prefix_sums[current_sum - targetSum]
            
            # 현재 누적합을 저장
            prefix_sums[current_sum] += 1
            
            # 왼쪽, 오른쪽 탐색 
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            
            prefix_sums[current_sum] -= 1
            
            return count

        # 루트 노드부터, 초기 누적합 0을 가지고 탐색 
        return dfs(root, 0)