import math
# 1. Area of a Circle
radius = float(input('Enter the radius of a circle : '))

area = math.pi * pow(radius, 2)

print(f'The area is {round(area, 2)}')

# 2. Circumference of a Circle
radius = float(input('Enter the radius of a circle : '))

circumference = 2 * math.pi * radius

print(f'The circumference is : {round(circumference, 2)}')

# 3. Pythagorean Theorem (Hypotenuse of a Right Triangle)
a = float(input('Enter side A : '))
b = float(input('Enter side B : '))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f'The Third side is : {round(c, 2)}')

# 4. Volume of a Sphere
radius = float(input('Enter the radius of the sphere : '))

volume = (4/3) * math.pi * pow(radius, 3)

print(f'The volume of the sphere is : {round(volume, 2)}')

# 5. Area of a Rectangle
length = float(input('Enter the length of the rectangle : '))
width = float(input('Enter the width of the rectangle : '))

area = length * width

print(f'The area of the rectangle is : {round(area, 2)}')

# 6. Area of a Triangle (Using Base and Height)
base = float(input('Enter the base of the triangle : '))
height = float(input('Enter the height of the triangle : '))

area = 0.5 * base * height

print(f'The area of the triangle is : {round(area, 2)}')

# 7. Cylinder Volume
import math

radius = float(input('Enter the radius of the cylinder : '))
height = float(input('Enter the height of the cylinder : '))

volume = math.pi * pow(radius, 2) * height

print(f'The volume of the cylinder is : {round(volume, 2)}')