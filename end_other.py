def end_other(a, b):
    if not a or not b :
        return True  
    lower_a, lower_b = a.lower(), b.lower()
    if len(lower_a) == len(lower_b):
        return lower_a == lower_b
    elif len(lower_a) < len(lower_b):
        print(lower_b[len(lower_b) - len(lower_a):])
        if lower_b[len(lower_b) - len(lower_a):] == lower_a:
            return True 
    else:
        print(lower_a[len(lower_a) - len(lower_b) :])
        if lower_a[len(lower_a) - len(lower_b) :] == lower_b:
            return True
    return False
  
print(end_other('abc', 'abXabc'))
print(end_other('Hiabc', 'abc'))