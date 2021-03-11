def rotate(str):
    i = 0
    str = list(str)
    while i < len(str) - 1:
        str[i],str[i+1] = str[i+1] ,str[i]
        i += 2
    print(''.join(str))
print(rotate("abc3qd1234567891"))



