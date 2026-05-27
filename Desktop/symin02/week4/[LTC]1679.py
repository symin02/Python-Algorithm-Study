class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        # 투 포인터를 쓰기 위해 배열을 오름차순 정렬
        nums.sort()

        left = 0
        right = len(nums) -1
        count = 0 # 합이 k가 되는 쌍의 개수
        
        # 양끝에서 포인터 좁혀오기
        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1 # 합을 키우기 위해 작은 쪽을 이동
            else:
                right -= 1 # 합을 줄이기 위해 큰 쪽을 이동

        return count
        