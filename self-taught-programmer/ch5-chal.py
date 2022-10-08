
'''
write a function that takes a number as an input and 
returns that number squared
'''
def square(num: int):
  return num**2

'''
createa a function that accepts a string as a parameter
and prints it
'''
def stringParam(string: str):
  print(string)
  
if __name__ == '__main__':
  print(square(2))
  stringParam("Howdy world!")