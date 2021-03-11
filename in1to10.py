def in1to10(n, outside_mode):
  if not outside_mode:
      return True if n in range(1,11) else False
  return True if n <= 1 or n >= 10 else False
 
