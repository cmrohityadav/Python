x=99
def f1():
    x=88
    def f2():
        print(x)
    return f2


result=f1()
print("result",result)
result()