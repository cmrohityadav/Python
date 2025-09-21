suger_amount=2
print(f"Initial sugar : {suger_amount}")

suger_amount=12
print(f"second initial sugar: {suger_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")
print(f"ID of 2: {id(2)}")



#---------immutable example---------

spice_mix=set()
print(f"initial spice mix id: {id(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("cardamon")

print(f"After spice mix id : {id(spice_mix)}")