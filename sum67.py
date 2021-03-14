def sum67(nums):
    result = 0 
    skip = False
    for num in nums:
        if num == 6:
            skip = True 
        if not skip :
            result += num 
        if num == 7:
            skip = False
    return result
