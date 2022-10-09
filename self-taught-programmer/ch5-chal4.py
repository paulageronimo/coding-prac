'''
write a program with two functions. 
'''

def first(num: int):
  """
  The first function should take an integer as a 
  parameter and return the result of the integer 
  divided by 2.
  """
  return num/2

def second(num: int):
  """
  The second function should take an integer as a parameter
  and return the result of the integer multiplied by 4.
  """
  return num * 4

if __name__ == '__main__':
  """
  Call the first funciton, save the result as a variable, and 
  pass it as a parameter to the second function.
  """
  var = first(5)
  print(var)
  
  var2 = second(var)
  print(var2)