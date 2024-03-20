def chaicoder(num):
    def actual(x):
        return x**num
    return actual

g=chaicoder(2)
f=chaicoder(3)
print(g)
print(f)
print(g(4))
print(f(4))
