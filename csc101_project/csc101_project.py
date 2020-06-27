#with statement automatically close file, opens file in read mode, file object referred to as x
# strip() removes lines 

with open('csc101_project/info.txt', 'r') as x:                
  info_text_data = [line.strip() for line in x] 
  print(info_text_data)

def modify_name(list, name):
  list[5] = name
  print(list)

modify_name(info_text_data, 'Stiven Cabrera' )
  


