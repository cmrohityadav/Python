tea_varities=["balck","green","white"]
 
for item in tea_varities:
        print(item)


for eachItem in tea_varities:
        print(eachItem,end="-")


if "oolong" in tea_varities:
        print("I have Oolong tea")

tea_varities.append("oolong")
if "oolong" in tea_varities:
    print("I have oolong after append")