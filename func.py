# a=9
# b=10
# c=sum((a,b))
# print(c)

# def function1():
#     print("hello world")

# function1()
# function1()
# function1()

# def func2(a,b):
#     avrg=(a+b)/2
#     return avrg

# print(func2(6,6))
# func_value=func2(5,7)
# print(func_value)


def function3(a, b):
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""
    average = (a+b)/2
    # print(average)
    return average

# v = function2(5, 7)
# print(v)
print(function3.__doc__)