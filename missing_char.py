def missing_char(char, n):
    char_arr = list(char)
    char_arr.pop(n)
    print(''.join(char_arr))
str = "kitten"
missing_char(str,1)
missing_char(str,0)
missing_char(str,4)