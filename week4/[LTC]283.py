class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero_idx = 0
        for i in range(len(nums)):
            #0이 아닌 숫자를 만나면
            if nums[i] != 0:
                #zero_idx 위치에 있는 값(0일 확률이 높은 값)과 현재 숫자의 위치를 맞바꿈
                nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
                # 0이 들어갈 다음 타켓 위치로 
                zero_idx += 1

        for j in range(zero_idx, len(nums)):
            nums[j] = 0