from fractions import Fraction

length, width = 2+Fraction(1, 4), 4+Fraction(7, 8)

print("length : " + str(length))
print("width  : " + str(width))

print(length >= width)

length, width = width, length

print("length : " + str(length))
print("width  : " + str(width))
print(length >= width)
