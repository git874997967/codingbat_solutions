def near_ten(num):
  return True if  10 + abs(num % 10) <= 12 or 10 + abs(num % 10) >= 18 else False
  
