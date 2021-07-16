def precedencia(string):
  if string == "+" or string == "-":
    return 1
  elif string == "*" or string == "/":
    return 2
  elif string == "^":
    return 3
  else:
    return -1