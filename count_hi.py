def count_hi(str):
    # base case
    if not str or len(str) <= 1:
        return 0
    if str == 'hi':
        return 1
    matchStr, result  = 'hi', 0
    for i in range(0,len(str) - 1):
        if str[i:i+2] == matchStr:
            result += 1
    return result
print(count_hi("abc hi hi"))