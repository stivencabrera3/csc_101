#if-else statements and boolean

temp = 39

# if temp >= 40:
#   print('It\'s nice outside')

# else:
#   print('It\'s cold outside')

# password = input('Enter password ')
# confirm_password = input('Re-enter password ')

# if password != confirm_password:
#   print('Passwords entered do not match.')
# else:
#   print('New password confirmed.') 


#Nested If Else, to check if multiple things are true or false

min_salary =  30000
min_years = 2

salary = int(input('What is your salary? '))
years = int(input('How many years have you worked at your current job? '))

# if salary >= min_salary and years >= min_years: 
#   print('You qualify!')
# else:
#   print('You do not qualify.')

#the above checks if BOTH conditions are true. Both conditions need to be true or else it fails and prints else.



if salary >= min_salary:
  if years >= min_years:
    print('You qualify')
  else:
    print(f'Sorry, you need to have worked for at least {min_years} years to qualify.')

else: 
  print(f'Sorry, you need to make at least {min_salary} to qualify.')

  #This code first checks if the first condition is true, and is so, checks if the next condition is true. If not, it returns else.