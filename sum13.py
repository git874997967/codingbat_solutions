def sum13(nums):
  if not nums:
      return 0
  result = 0  
  skip = False
  for num in nums:
      if num != 13 and not skip:
          result += num  
          skip = False
      elif num == 13:
          skip = True 
      else:
        skip = False
  return result
