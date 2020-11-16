from sympy import *

x = Symbol("x")
print("The solution set for 4sin(x)cos(x) = √3 is as follows:")
pprint(solveset(Eq(4 * sin(x) * cos(x), sqrt(3)), x),use_unicode = True)

print("The solution set for cos(2x)−cos(x) = 0 is as follows:")
pprint(solveset(Eq(cos(2 * x) - cos(x), 0), x),use_unicode = True)
