def string_splosion(str):
    result = ''
    for i in range(len(str)+1):
        result += str[0:i]
 
    return result
  
print(string_splosion("code"))