chai_types={"masala":"Spicy","ginger":"Zesty","Green":"mild"}

print(len(chai_types))

chai_types["lemon"]="citrus"

print(chai_types)

print(chai_types.pop("Green"))
print(chai_types)

print(chai_types.popitem())

print(chai_types)

del chai_types["ginger"]
print(chai_types)

chai_types_copy=chai_types.copy()

