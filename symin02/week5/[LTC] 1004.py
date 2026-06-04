class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeros_cnt = 0  # 현재 구간 안의 0의 개수
        max_count = 0  # 조건을 만족하는 최대 길이
        left = 0
        
        # for문으로 오른쪽 값을 하나씩 현재 구간에 포함시킴
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_cnt += 1
            
            # 0이 k개보다 많다면 왼쪽 값을 하나 뻄
            while zeros_cnt > k:
                if nums[left] == 0:
                    zeros_cnt -= 1
                left += 1  # 왼쪽을 오른쪽으로 한 칸 당김
                
            # 현재 구간 길이 = right - left + 1(현재 크기)
            current_length = right - left + 1
            max_count = max(max_count, current_length)
            
        return max_count