class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # 1. 맨 첫 번째 창문(0부터 k까지)의 합 구하기
        current_sum = sum(nums[:k]) 
        max_sum = current_sum 

        # 2. 인덱스 k부터 시작해서 창문을 오른쪽으로 한 칸씩 밀기
        for i in range(k, len(nums)):
            # 들어오는 거 더하고, 나가는 거 빼기
            current_sum = current_sum + nums[i] - nums[i - k]
                                      
            # 3. 최대 합 갱신하기
            max_sum = max(max_sum, current_sum)
        # 최댓값을 k로 나누어 평균 구하기(정수 나눗셈 말고 실수 나눗셈 / 사용)
        return max_sum / k
    