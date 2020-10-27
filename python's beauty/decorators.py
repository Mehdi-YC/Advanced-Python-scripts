import time

def time_it(func):
  def wrapper(*args,**kwargs):
      start = time.time()
      result = func(*args,**kwargs)
      end= time.time()
      print("it took {} ms".format((end-start)*1000))
      
      return result
      
  return wrapper
  
@time_it 
def mul(*args):
  r=1
  for i in args:
    r*=i
  print(r)
  
@time_it
def printing(f):
  print(f.__name__,dir(f))
    
    
printing(mul)

  