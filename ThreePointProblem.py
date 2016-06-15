import os, math



print("_______________________________________________\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Three Point Problem Solver")
print("Scott D. Hull, 2016\n")
print("Please enter your highest point (in ft).")
highpoint = float(input(">>> "))
print("\nPlease enter your lowest point (in ft).")
lowpoint = float(input(">>> "))
print("\nPlease enter your intermediate point (in ft).")
intpoint = float(input(">>> "))
print("\nPlease enter the distance between your highest and lowest points (in ft).")
dist_highlow = float(input(">>> "))
diff_highlow = highpoint - lowpoint
# print("Diff_highlow: " + str(diff_highlow))
appdip_math = diff_highlow / dist_highlow
apparentdip = math.degrees(math.atan(appdip_math))
print("\nThe apparent dip is: " + str(apparentdip) + " degrees.")
apparentdip_tan = math.tan(math.radians(apparentdip))
# print("apparantdip_tan: " + str(apparentdip_tan))
diff_highint = highpoint - intpoint
# print("Diff_highint: " + str(diff_highint))
dist_intintersect = diff_highint / apparentdip_tan
print("The distance from the high point to the point of intersection is: " + str(dist_intintersect) + " ft.")
# intersection = dist_highlow - dist_intintersect
# print("The point of intersection is at: " + str(intersection))
print("\nPlease enter the angle to where a line drawn from the highest point intersects the strike (in degrees).")
angle2strike_in = float(input(">>> "))
angle2strike = math.cos(math.radians(angle2strike_in))
dist_newline = angle2strike * dist_intintersect
print("\nThe distance from high point to strike is: " + str(dist_newline) + " ft.")
#______________True dip calculation below
val1 = diff_highint / dist_newline
truedip = math.degrees(math.atan(val1))
print("The true dip is: " + str(truedip) + " degrees.")
print("\n_______________________________________________\n")