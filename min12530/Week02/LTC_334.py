class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = None
        second = None
        
        for num in nums:
            # 1. first가 아직 비어있거나, 현재 숫자가 first보다 작거나 같을 때
            if first is None or num <= first:
                first = num
            # 2. second가 아직 비어있거나, 현재 숫자가 second보다 작거나 같을 때
            elif second is None or num <= second:
                second = num
            # 3. 위 두 조건을 다 통과했다면 세 번째로 큰 수를 찾은 것!
            else:
                return True
                
        return False
