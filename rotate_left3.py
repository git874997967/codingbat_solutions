def rotate_left3(nums):
  result = nums[1:]
  result.append(nums[0])
  return result
  