'''
write a program with two functions. 

The first function should take an integer as a 
parameter and return the result of the integer 
divided by 2.

The second function should take an integer as a parameter
and return the result of the integer multiplied by 4.

Call the first funciton, save the result as a variable, and 
pass it as a parameter to the second function.
'''
def first(num: int):
  return num/2

def second(num: int):
  return num * 4

if __name__ == '__main__':
  var = first(5)
  print(var)
  
  var2 = second(var)
  print(var2)