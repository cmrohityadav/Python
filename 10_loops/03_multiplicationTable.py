number=int(input("NUmber: "))

for i in range(1,11):
    if i==5: 
        continue
    print(number,"X",i,"=",i*number)