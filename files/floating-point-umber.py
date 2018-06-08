""" 3.14149236
6.22E12

these are ordinary double precision floating point numbers. It's important to remember
that floating point point values
are only approximations, They usually have a 64 bit implementation.
"""


""" How to know which compiler was used by to make python.
This will tell us about what floating point libraries are used. This will help determine
which under lying mathematical libraries are in use.
"""

import platform

print(platform.python_build())
print()
print(platform.python_compiler())
