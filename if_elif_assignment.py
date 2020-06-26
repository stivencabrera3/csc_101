num1 = float(input('Enter first value '))
num2 = float(input('Enter second value '))

operation = input('Which operation would you like to perform? \n1 for addition\n2 for subtraction\n3 for division\n4 for multiplication ')

if operation == '1':
  print(num1 + num2)
elif  operation == '2':
  print(num1 - num2)
elif  operation == '3':
  print(num1 / num2)
elif  operation == '4':
  print(num1 * num2) 
else: 
  print('Invalid selection') 