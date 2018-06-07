
""" We were sent out to track down a missing device.
  Details of thw device are strictly need-to-know.
  Since we are new agents, all that HQ will release to us
   is the overall size in square inches.

   Here's an exact calculation of the area of a device we found.
   It is measured as 4 7/8  multiplied by 2 1/4
"""

from fractions import Fraction
length = 4 + Fraction("7/8")
width = 2 + Fraction("1/4")

area = length * width

print(area)
# print(type(area)) --> <class 'fractions.Fraction'>

""" divmod() function gives us quotient and a remainder 
     and it returns tuple
"""

print((divmod(351, 32)))
