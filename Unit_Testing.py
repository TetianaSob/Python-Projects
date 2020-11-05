# Unit_Testing.py

from math import pi


def circle_area(r):
    return pi*(r**2)

#Testing
radii = [2, 0, -3, 2+5j, True, "radius"]
message="Area of circles with r = {radius} is {area}." 

for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))

# Area of circles with r = 2 is 12.566370614359172.
# Area of circles with r = 0 is 0.0.
# Area of circles with r = -3 is 28.274333882308138.
# Area of circles with r = (2+5j) is (-65.97344572538566+62.83185307179586j).
# Area of circles with r = True is 3.141592653589793.
# Traceback (most recent call last):
#   File "d:/MY STUFF/Online courses/Python/FirstProgram/Unit_Testing/Unit_Testing.py", line 
# 12, in <module>
