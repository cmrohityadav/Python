def fac(a):
    if a==0 or a==1: return a
    return fac(a-1)*a

print(fac(5))