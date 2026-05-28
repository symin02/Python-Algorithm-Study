def moveZeroes(nums):

    zero_idx = 0
    for i in range(len(nums)):
        # 0이 아닌 수를 만나면 덮어쓰기
        if nums[i] != 0:
            nums[zero_idx] = nums[i]
            # print(f'nums: {nums}, i: {i}, idx: {zero_idx}')
            zero_idx += 1

    # 덮어쓰고 남은 부분 0으로 채우기
    for j in range(zero_idx, len(nums)):
        nums[j] = 0

# moveZeroes([0, 1, 0, 2, 3, 4, 5])


