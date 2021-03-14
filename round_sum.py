def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)


def  round10(n):
    return  (( n% 10) + 1) * 10 if  (n % 10) >= 5 else  (( n% 10) - 1) * 10
