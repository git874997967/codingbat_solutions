def lucky_sum(a, b, c):
  sum = a + b + c  
  if  a == 13:
      return 0 
  elif b == 13:
      return a   
  elif c == 13:
      return a + b 
  return sum 
