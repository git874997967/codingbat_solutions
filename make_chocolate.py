def make_chocolate(small, big, goal):
  count_big = goal // 5
  if count_big > big:
      if big * 5 + small < goal :
          return -1
      else:
          return goal - big * 5
  return True if (goal - count_big * 5 ) < small else  False

# make_chocolate(3, 1, 9) → -1
# make_chocolate(1, 2, 7) → -1