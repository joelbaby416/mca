import math
def area_of_the_circle(radius):
	area=radius**2*math.pi
	return area
radius=float(input("please enter the radius:"))
print("The area of the given circle is:",area_of_the_circle(radius))
