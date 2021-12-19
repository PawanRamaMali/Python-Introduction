# #x = "awesome"

# def myfunc():
#   print("Python is " + x)

# #myfunc()

x = "awesome"  # Global Variable 
x, y = 10,20 # Global
 
# Function definition 
def myfunc2():
  global x, y
  global = 5 
  x = 2
  y = 4
  print(x) # Local scope 
  print(y)
  print("Sum is " + str(x + y))

myfunc2() # Function Call 
print("Sum outside is " + str(x + y))

# wHAT IS KEYWORD IN PYTHON ? EXAMPLS : global def print 
