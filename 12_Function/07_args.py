# *args

def sumAll(*args):
     print(args)
     for i in args:
          print(i)
     return sum(args)


# print(sumAll(1,2))
print(sumAll(1,2,3))
# print(sumAll(1,2,3,4))