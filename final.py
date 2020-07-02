def height_for_rides():
  name = 'Stiven Cabrera'

  feet = int(input('Enter your height in feet: '))
  inches = int(input('Enter your height in inches: '))

  message_list = ['Yay! You can get on the rides alone', 'You must be accompanied by an adult', f'Sorry you\'re not allowed on the rides - {name} ']

  if feet >= 5:
    print(message_list[0])

  if feet < 5:
    if feet == 4:
      if inches >= 1:
        print(message_list[1])
      elif inches == 0:
        print(message_list[2])
    
    elif feet < 4:
       print(message_list[2])
  
height_for_rides()