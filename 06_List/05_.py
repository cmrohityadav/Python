tea_varities=["balck","green","oolong","white"]

print(tea_varities)
teacopy=tea_varities
print(teacopy)\

print(tea_varities is teacopy)

teacopyTwo=tea_varities.copy()
print(teacopyTwo)
print(tea_varities is teacopyTwo)