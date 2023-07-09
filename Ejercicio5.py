def bisiesto(ano):
  if ano % 4 ==  0:
    return True
  else:
    if (ano % 100 == 0) and (ano % 400 != 0):
      return False
  return False

print(bisiesto(2024))