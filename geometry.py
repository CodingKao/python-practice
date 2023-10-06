# Geometry

# variables 
a = 5 
b = 6
c = 7

# Calculate perimeter of triangle
perimeter = a + b + c

# print statement using f'strings
print(f'A triangle with sides of {a}, {b}, and {c} has a perimeter of {perimeter}.')

# calculate area formual = .5 * b *h
base = c
height = b

area = .5 * (base * height)
print(f'A triangle with a base of {base} and a height of {height} has an area of {area}.')

'''1.3 assign variable to represent radis of circle
# use constant of 'pi' contained within math module and radius variable
# to calculate the circuference and area of a circle'''

# import math for 'pi' constant
import math

# assign radius
radius = 5

# calculate the circumference and area
circumference = 2 * math.pi * radius

area_2 = math.pi * (radius ** 2)

print(f'''
Circle

Radius: {radius}
Circumference: {circumference}
Area: {area_2}''')

# calculate the volumn of a sphere with same radius
volume = (4/3) * math.pi * (radius **3)
print(f'''
Sphere

Radius: {radius}
Volume: {volume}
''')

# assign a number to a variable to represent the radius of a second circle.
# Use the tow radii to calculate the area of an annulus

# outer and inner radii
outer_radius = 5
inner_radius = 3

# calculate the area
annulus_area = math.pi * (outer_radius **2 - inner_radius ** 2)
print(f'''
Annulus

OUter radius: {outer_radius}
Inner radius: {inner_radius}

Area: {annulus_area}

''')

# create two variables, x and y to represent the adjacent sides of a right triangle.
# Find the hypotenuse of a triangle using, x and y.  Assign the value to a variable z.
# Display the result to the user
x = 3
y = 4

# calculate the hypotenuse with Pythagoream Theorem
hypotheuse = math.sqrt(x**2 + y**2)

# print using f-string
print(f'''
A triangle adjacent sides of {x} and {y} has a hypotenuse of {hypotheuse}.
''')

