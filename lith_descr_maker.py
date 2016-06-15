import os, sys, csv


home_dir = []
home_dir.append(os.getcwd())

print("\n__________________________________\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Litholigic Unit Description Maker")
print("Scott D. Hull, 2016")
print("\n\nPlease enter the following prompts.  Press 'enter' on questions you'd like to skip.\n")

if "Lithologic_Description.txt" in os.listdir(os.getcwd()):
    os.remove("Lithologic_Description.txt")
else:
    pass
outputfile = open("Lithologic_Description.txt", 'a')


x0 = input("Lithostratigraphic Name: ")
outputfile.write(x0 + "\n\n")


print("\n\n\nThese questions will be asked in the following order:")
print("Lithology")
print("Slope/Ledge/Cliff forming")
print("Color")
print("Bed thickness")
print("Induration")
print("Grain size")
print("Grain sorting")
print("Grain shape")
print("Grain composition")
print("Cement")
print("Fossils")
print("Definition of contact(s)")
print("Unit thickness")
print("Structures")
print("Way up")
print("Other features\n\n")

def lithloop():
    print("\n")
    x1 = input("Lithology: ")
    x17 = input("Slope/Ledge/Cliff forming: ")
    x2 = input("Color: ")
    x3 = input("Bed thickness: ")
    x4 = input("Induration: ")
    x5 = input("Grain size: ")
    x6 = input("Grain sorting: ")
    x7 = input("Grain shape: ")
    x8 = input("Grain composition: ")
    x9 = input("Cement: ")
    x10 = input("Fossils: ")
    x11 = input("Definition of contact(s): ")
    x12 = input("Unit thickness: ")
    x15 = input("Structures: ")
    x16 = input("Way up: ")
    x14 = input("Other features: ")
    def endloop():
        x13 = input("\nWould you like to add another lithology?  Enter 'y' or 'n': ")
        if x13 == "y":
            if x14 == "":
                output_strings = x1 + ", " + x17 + ", " + x2 + ", " + x3 + ", " + x4 + ", " + x5 + ", " + x6 + ", " + x7 + ", " + x8 \
                 + ", " + x9 + ", " + x10 + ", " + x11 + ", " + x12 + ", " + x15 + ", " + x16 + ".  "
                outputfile.write(output_strings)
                lithloop()
            else:
                output_strings = x1 + ", " + x17 + ", " + x2 + ", " + x3 + ", " + x4 + ", " + x5 + ", " + x6 + ", " + x7 + ", " + x8 \
                 + ", " + x9 + ", " + x10 + ", " + x11 + ", " + x12 + ", " + x15 + ", " + x16 + ", " + x14 +  ".  "
                outputfile.write(output_strings)
                lithloop()
        elif x13 == "n":
            if x14 == "":
                output_strings = x1 + ", " + x17 + ", " + x2 + ", " + x3 + ", " + x4 + ", " + x5 + ", " + x6 + ", " + x7 + ", " + x8 \
                 + ", " + x9 + ", " + x10 + ", " + x11 + ", " + x12 + ", " + x15 + ", " + x16 + "."
                outputfile.write(output_strings)
            else:
                output_strings = x1 + ", " + x17 + ", " + x2 + ", " + x3 + ", " + x4 + ", " + x5 + ", " + x6 + ", " + x7 + ", " + x8 \
                 + ", " + x9 + ", " + x10 + ", " + x11 + ", " + x12 + ", " + x15 + ", " + x16 +  ", " + x14 + "."
                outputfile.write(output_strings)
        else:
            print("\nOops!  That's not a valid option!\n")
            endloop()
    endloop()

lithloop()

outputfile.close()

print("\n\n\n\nHere is your lithologic description of " + x0 + ":\n")
f = open("Lithologic_Description.txt", 'r')
file_contents = f.read()
print(file_contents)
f.close()
print("\n\n'Lithologic_Description.txt' now available in '" + home_dir[0] + "'.")
print("\n\nExiting script...\n__________________________________\n")
