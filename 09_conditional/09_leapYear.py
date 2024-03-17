year=int(input("Year: "))

if (year%4==0 and year%100!=0 ) or (year%400==0):
    print("this ",year, "this leap year")
else:
    print(year," year not leap year")