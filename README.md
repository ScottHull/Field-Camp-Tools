# Field-Camp-Tools
Tools I made at OSU Geology Field Camp, 2016.


_________________________________________________________________________________________________________________
TOOL 1: THREEPOINTPROBLEMI.PY

Three Point Problem Solver (work in progress)

Assists in the construction of a classic three point problem in geology.

By: Scott D. Hull, Field Camp 2016


This code is meant to be launched with Python 3 via the command terminal and is meant to be a calculator while the user is manually drawing the three point problem.

When prompted, enter (in feet) the elevation of your highest point, your lowest point, and an intermediate point.  Then, enter the distance (in feet) from the lowest point to the highest point.  The code will calculate and display the apparant dip as well as the distance from the highest point to the point where strike would intersect the line between the highest and lowest point.

Once this strike line is drawn on your paper, draw a line perpendicular from the strike line to the highest point.  This should form a right triangle.  Take the angle from the highest point to the strike line (within the right triangle) and enter when prompted.  The code will calculate both the distance of this leg of the triangle (the distance from the highest point to where your perpendicular line intersects the strike line) as well as the true dip.


Disclaimer: This code is not finished.  Please check your work and report any problems with the code to me.



_________________________________________________________________________________________________________________
TOOL 2: QUAD2AZI.PY

Quadrant to Azimuth Converter.

Converts quadrant compass measurements to azimuth.

By: Scott D. Hull, Field Camp 2016 (yeah, I got the quadrant compass)

Boot up 'quad2azi.py' with Python 3 via the command terminal.

Enter in a '.csv' file existing in the same directory as the python script at the prompt, formatted so that your quadrant measurements are in a single column, like in the following example:

N60W

S20E

N68E

The code will convert quadrant to azimuth notation and output a file called 'Quad2Azi_Out.csv', in which your quadrant measurements will be in the first column and the corresponding azimuth notation in the second.



_________________________________________________________________________________________________________________
TOOL 3: LITH_DESCR_MAKER.PY

Lithologic Description Maker.

Prints out an ordered lithologic description.

By: Scott D. Hull, Field Camp 2016

Boot up 'lith_descr_maker.py' in the command terminal with Python 3.

Enter in lithologic descriptions as prompted, and you may enter as may as you'd like per lithostratigraphic unit.  A proper, ordered lithologic description will be printed at the end at saved to a file called "Lithologic_Description.txt'.  This file will be deleted and recreated the next time the script is booted up.



_________________________________________________________________________________________________________________
TOOL 4: APPARENTDIPCALCULATOR.PY

Calculates apparent dip given true dip and angle between strike line and strike.

By: Scott D. Hull, Field Camp 2016

Boot up "apparentdipcalculator.py' in the command terminal with Python 3.  Please make sure that all inputs, incluidng in .csv inputs, are in degrees.

Enter either 'input' to manually enter in true dip and the angle between strike and the cross section line one at a time, or enter 'csv' to input a .csv file with multiple pairs of values.  If inputting a .csv file, make sure that true dip is in the first column and the angle between the strike and the cross section line is in the second line.  If using the .csv input, the program will not only output apparant dip to the screen but will write a file named "apparent_dip_outputs.txt' which will include true dip in the first column, the angle between the strike and the cross-section line in the second column, and the apparent dip in the third column.
