class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c_sum = sum(nums[:k])
        m_sum = c_sum

        for i in range(k, len(nums)):
            c_sum = c_sum + nums[i] - nums[i-k]
            
            if c_sum > m_sum:
                m_sum = c_sum
        
        return m_sum/k