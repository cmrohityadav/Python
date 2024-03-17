number=int(input("Number: "))

sumEven=0

for i in range(1,number+1):
    if i%2==0:
        sumEven+=i

print("sum of even number is ",sumEven)