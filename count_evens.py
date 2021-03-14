def count_evens(nums):
  result = 0
  for num in nums:
      if num % 2 == 0:
          result += 1
  return result
