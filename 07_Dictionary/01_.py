chai_types={"masala":"Spicy","ginger":"Zesty","Green":"mild"}

print(chai_types)


print(chai_types["masala"])

print(chai_types.get("masala"))
print(chai_types.get("Masala"))
print(chai_types.get("Sasala"))

chai_types["Green"]="fresh"
print(chai_types)