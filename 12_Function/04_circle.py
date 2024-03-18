import math
def circle(radius):
    area= math.pi*radius**2
    circumference=2*math.pi*radius
    return area,circumference


areaofCircle,circumfereceOfCircle=circle(5)

print("area: ",areaofCircle," circumference: ",circumfereceOfCircle)
