from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start= 0
        end = len(nums) - 1
        rem = []
        
        while start < end:
            # 두 포인터가 가르키는 값들의 합과 k가 같다면 index 저장 후 각각 포인터 옮기기
            if nums[start] + nums[end] == k:
                rem.append(start)
                rem.append(end)
                start += 1
                end -= 1
            
            # 합이 k보다 크다면 값을 줄이기 위해 end 포인터 1 감소
            elif nums[start] + nums[end] > k:
                end -= 1

            # 합이 k보다 작다면 값을 늘리기 위해 start 포인터 1 증가
            else:
                start += 1

        # 조건을 만족한 index들이 있는 배열 길이를 2로 나눔s
        return len(rem) // 2

s = Solution()
print(s.maxOperations([3,1,3,4,3], 6))