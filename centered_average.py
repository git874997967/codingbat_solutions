def centered_average(nums):
  result = 0 
  maxNum , minNum = max(nums), min(nums)
  for num in nums:
      result += num 
  return (result - maxNum - minNum ) / (len(nums) -2)
