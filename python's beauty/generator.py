#simple list as result (return):
def square_num_list(*args):
  result=[]
  for i in args:
    result.append(i*i)
  return(result)
print("with normal list :")
print(square_num_list(1,4,5))


# --------------------------------------------
#generators (yield):
def square_num_generator(*args):
  for i in args:
    yield i*i
    
print("\nwith generators :")
print(square_num_generator(1,4,5))
result = square_num_generator(1,4,5)
print(next(result))
print(next(result))
print("i can dpo whatever i want in between ")
print(next(result))

# --------------------------------------------
#list comprehension :
args = [1,4,5]
result = [x*x for x in args]
print(result)
#list comprehension like generator :
args = [1,4,5]
result = (x*x for x in args)
print(result)


#going crazy
square_num_generator = lambda *x: [i*i for i in x]
square_num_generator_lc = lambda *x: (i*i for i in x)
print("this is crazy")
result1 = square_num_generator(1,4,5)
result2 = square_num_generator_lc(1,4,5)
print(result1)
print(result2)
print(next(result2))
print(next(result2))

#_____________________________
#testing some labda stuff : 

ok =lambda y:list(filter(lambda x:x%2==2,y))
print(ok([1,4,5,8,9]))


print([x for x in  range(10) if x> 5 and x%2==0])





