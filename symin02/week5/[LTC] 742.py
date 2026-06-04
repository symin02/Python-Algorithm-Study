from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)   # 배열 전체의 총합을 미리 구해둠
        left_sum = 0            # 현재 내가 서 있는 인덱스의 왼쪽 구간 합

        # 한 칸씩 이동하며 탐색
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            
            # 왼쪽 합과 오른쪽 합이 똑같다면 피벗 인덱스
            if left_sum == right_sum:
                return i
            
            # 다음 칸으로 넘어가기 전에 현재 내 값을 왼쪽 합에 누적해서 더해줌
            left_sum += nums[i]
            
        # 다 돌았는데 똑같은 지점을 못 찾았다면 -1 리턴
        return -1
    
    #~742