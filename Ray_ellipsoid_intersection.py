# full_ops.py
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# Text explaining script usage
# Parameters: d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# Output:
# A description of the script output
#
# Written by Devon Throckmorton

# import Python modules
import math # math module
import sys
from math import dot # argv
from math import smul # argv
from math import add # argv
import numpy
R_E_KM = 6378.137  # Earth's semi-major axis in km
E_E = 0.081819221456  # Earth's eccentricity
w = 7.292115 * 10**(-5) # rad/s
# initialize script arguments
d_l_x = float('nan')    
d_l_y = float('nan')        
d_l_z = float('nan')
c_l_x = float('nan')
c_l_y = float('nan')    
c_l_z = float('nan')        
if len(sys.argv) == 7:
    d_l_x = sys.argv[1]    
    d_l_y = sys.argv[2]        
    d_l_z = sys.argv[3]
    c_l_x = sys.argv[4]
    c_l_y = sys.argv[5]    
    c_l_z = sys.argv[6]        
else:
    print('Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z')
    exit()

vector = numpy.array
d_l = vector([d_l_x, d_l_y, d_l_z])
c_l = vector([c_l_x, c_l_y, c_l_z])
a = dot(d_l, d_l)
b = 2.0*dot(d_l,c_l)
c = dot(c_l,c_l)
discr = b*b-4.0*a*c
if discr>=0.0:
    d = (-b-math.sqrt(discr))/(2.0*a)
if d<0.0:
    d = (-b+math.sqrt(discr))/(2.0*a)
if d>=0.0:
    l_d = add(smul(d,d_l),c_l)

print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point