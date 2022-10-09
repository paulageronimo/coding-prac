
def square(num: int):
  """
  write a function that takes a number as an input and 
  returns that number squared
  """

  return num**2


def stringParam(string: str):
  """
  createa a function that accepts a string as a parameter
  and prints it
  """
  print(string)
  

def params(x:int, y:int, z:int, a=1, b=2):
  """
  write a function that takes three required parameters
  and two optional parameters
  """
  print(x, y, z, a, b)

def str2float(string: str):
  """
  write a function that converts a string to a float and returns
  the result. 

  use exception handling to catch the exception that
  could occur.
  """
  try:
    flt = float(string)
  except ValueError:
    return "Invalid input. Please try again with only numbers as a string."
  return flt

if __name__ == '__main__':
  print(square(2))
  stringParam("Howdy world!")
  params(10, 20, 30)
  params(10, 20, 30, 40, 50)
  print(str2float("Hi! 22"))
  print(str2float("!0"))
  print(str2float("22"))
  print(str2float("2.2"))