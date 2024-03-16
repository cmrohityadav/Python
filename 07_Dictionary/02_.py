chai_types={"masala":"Spicy","ginger":"Zesty","Green":"mild"}

# printing the key 
print("printing the key ")
for chai in chai_types:
    print(chai)

print("printing the value")

for element in chai_types:
    print(chai_types[element])

# print key and value 
print("print key and value ")
for key,value in chai_types.items():
    print(key,value)

