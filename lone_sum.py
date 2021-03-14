def lone_sum(a, b, c):
  sum = a + b + c 
  if a == b and a == c :
      return 0 
  if  a == b:
     return c 
  elif  a == c:
     return b 
  elif  c == b:
       return a 
  return  sum
