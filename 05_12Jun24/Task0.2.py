"""
3 sides are equal = equilateral
2 sides are equal = isosceles
no sides are equal =  scalene
"""

def triangle_sides(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    if side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
  #  elif side1 == 0 or side2 == 0 or side3  == 0:
   #     return "Invalid data"
    else:
        return "Scalene"

# Enter the value
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

triangle_type = triangle_sides(side1, side2, side3)
print(f"The triangle is: {triangle_type}")
