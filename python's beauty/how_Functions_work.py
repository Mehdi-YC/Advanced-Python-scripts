def add(x,y=10):
  '''this is not wtf'''
  return x+y
  
add10 = add

print(add10(10))


def call_method(f,x,y):
  print(f.__name__,f.__doc__,x,y)
  print(f(x,y))
  
print(call_method(add10,15,10))

