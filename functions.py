#First you define the function. Defining the fuction does not call it or execute. Just tells computer what the functon/what it does. 

def message():
  print('I am Arthur,\nKing of the Britons.')
   
#calling the function

message()

def main():
  value = 5
  show_double(value)

def show_double(number):
  result = number * 2
  print(result)
  
main()
