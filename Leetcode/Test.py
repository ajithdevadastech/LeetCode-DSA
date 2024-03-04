def divisor(n):
  return lambda a : a / n
temp = divisor(300)

print(temp(900))