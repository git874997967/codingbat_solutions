def xyz_there(str):
  if not str or len(str) < 3:
      return False
  if str[0:3] == 'xyz':
    return True
  for i in range(0,len(str) - 3):
       
      subStr = str[i:i+4]
      if subStr[0] != '.' and subStr[1:] == 'xyz':
          return True 
  return False