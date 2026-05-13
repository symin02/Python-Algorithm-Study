class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # 1. 왼쪽부터 누적 곱 구하기
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
            
        # 2. 오른쪽부터 역순으로 누적 곱 구해서 기존 answer에 곱하기
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
            
        return answer
