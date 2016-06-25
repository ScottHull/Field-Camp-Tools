import os, math, csv, time

print("\n__________________________________________________________\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Apparent Dip Calculator")
print("Scott D. Hull, Field Camp 2016\n\n")
print("Please enter all information in degrees!\n")


def inputthevalues():
    print("Please enter your true dip.")
    truedip = float(input(">>> "))
    print("\nPlease enter the angle between the cross-section line and the strike.")
    strikeangle = float(input(">>> "))

    apparentdip = math.degrees(math.atan(math.tan(math.radians(truedip))*math.sin(math.radians(strikeangle))))

    print("\nThe apparent dip is: " + str(apparentdip) + "\n")
    time.sleep(1)
    inputthevalues()


def inputcsv():
    if "apparent_dip_outputs.txt" in os.listdir(os.getcwd()):
        os.remove("apparent_dip_outputs.txt")
    else:
        pass
    outputfile = open("apparent_dip_outputs.txt", 'a')
    header = "TRUE DIP,ANGLE BETWEEN STRIKE AND CROSS SECTION LINE,APPARENT DIP"
    outputfile.write(header + "\n")
    print("\nPlease format columns so that true dip is in column 1 and angle between strike and cross-section line is in column 2.\n\n")
    print("Please enter your .csv filename in the working directory...")
    csvfile = input(">>> ")
    if csvfile in os.listdir(os.getcwd()):
        print("\n" + csvfile + " has been found in the working directory!\n")
        rawvals_truedip = []
        rawvals_strikeangle = []
        errors = []
        with open(csvfile, 'r') as infile:
            reader = csv.reader(infile, delimiter=",")
            for row in reader:
                try:
                    rawvals_truedip.append(float(row[0]))
                    rawvals_strikeangle.append(float(row[1]))
                    print("Got pair: " + row[0] + ", " + row[1])
                except:
                    print("An error has been found with pair " + row[0] + ", " + row[1] + ".  Skipping...")
                    pass
        infile.close()
        print("\n\n\n")
        print("TRUE DIP, ANGLE BETWEEN STRIKE AND CROSS SECTION LINE, APPARENT DIP\n")
        for i in rawvals_truedip:
            try:
                indexval = rawvals_truedip.index(i)
                truedip = rawvals_truedip[indexval]
                strikeangle = rawvals_strikeangle[indexval]
                apparentdip = math.degrees(math.atan(math.tan(math.radians(truedip))*math.sin(math.radians(strikeangle))))
                printout = str(truedip) + ", " + str(strikeangle) + ", " + str(apparentdip)
                print(printout)
                outputlist = []
                outputlist.append(truedip)
                outputlist.append(strikeangle)
                outputlist.append(apparentdip)
                wr = ",".join(str(z) for z in outputlist)
                outputfile.write("%s\n" % wr)
            except:
                print("An error has occured.  Likely an indexing error.  Please check your file for complete information.  Skipping...\n")
                pass
        outputfile.close()
        print("\nOutputs written to 'apparent_dip_outputs.txt' and available in path: ")
        print(os.getcwd())
        print("\n\n\nExiting script...\n\n")
        print("\n__________________________________________________________\n\n")
    else:
        print("\n" + csvfile + " has NOT been found in the working directory!\n")
        inputcsv()


def initialization():
    print("Would you like to enter information in the terminal or input a .csv file?")
    print("Please enter 'input' or 'csv'.")
    choice1 = input(">>> ")
    if choice1 == "input":
        print("\nPress 'CTRL + C' when you are finished...\n")
        inputthevalues()
    elif choice1 == "csv":
        inputcsv()
    else:
        print("Oops!  That's not a valid choice!\n")
        initialization()



initialization()


