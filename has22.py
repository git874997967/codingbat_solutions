def has22(nums):
 if len(nums) <2 :
     return False
 if len(nums) == 2 and nums !=[2,2]:
     return False
 for i in range(len(nums) - 1):
     if [nums[i],nums[i+1]] == [2,2]:
         return True
 return False 
