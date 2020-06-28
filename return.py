def calculator(operation, num1, num2):
  if operation == '+':
    result = num1 + num2
  elif operation == '-':
    result = num1 - num2
  elif operation == '/':
    result = num1 / num2
  elif operation == '*':
    result = num1 * num2
  
  return result 

print(calculator('*', 2, 5))







