def array123(nums):
  matchArr = [1,2,3]
  if len(nums) < 3:
      return False
  for i in range(len(nums)-2):
      print(nums[i:i+3])



arr = [1,1,2,3,1,4,5,6,7]
print(array123(arr))