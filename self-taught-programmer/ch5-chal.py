
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
  
'''
write a function that takes three required parameters
and two optional parameters
'''
def params(x:int, y:int, z:int, a=1, b=2):
  print(x, y, z, a, b)

if __name__ == '__main__':
  print(square(2))
  stringParam("Howdy world!")
  params(10, 20, 30)
  params(10, 20, 30, 40, 50)