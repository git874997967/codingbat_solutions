def array_front9(nums):
    if len(nums) >= 4:
        nums = nums[0:3]
    for num in nums:
        if num == 9:
            return True
    return False
