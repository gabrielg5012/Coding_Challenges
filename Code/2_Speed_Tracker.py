"""
Create a program that takes a time for a car going past a speed camera, 
the time going past the next one and the distance between them 
to calculate the average speed for the car in mph. The cameras are one mile apart.

EXTENTION:
1. Speed cameras know the timings of each car going past, through number 
plate recognition. Valid number plates are two letters, two numbers 
and three letters afterwards, for
example XX77 787. Produce a part of the program that checks whether 
a number plate matches the given pattern. Tell the user either way.


2. Create a program for creating a file of details for vehicles exceeding 
the speed limit set for a section of road. You will need to create a suitable 
file with test data, including randomised number plates and times. 
You will then use the code you’ve already written to process this list to 
determine who is breaking the speed limit (70mph) and who has invalid number plates.
"""

def CheckingValidPlate(plateNum):
    plateNumBool = False
    if len(plateNum) == 7:
        if plateNum[0:2].isdigit() == False:
            if plateNum[2:5].isdigit() == True:
                if plateNum[5:7].isdigit() == False:
                    plateNumBool = True
    return plateNumBool

def SpeedCalculator(time):
    speed = 1 / (time / 3600)
    return speed

def Recorder():
    f = open("...", 'a') # replace '...' with the location of a .txt file
    f.write("License Plate: #" + plateNum + "\n" + "Speed: " + str(speed)[0:4] + " mph" +"\n" + "Speeding OR Not: " + str(speedBool) + "\n" + "\n")
    f.close()

def ReadRecord():
    f = open("...", 'r') # replace '...' with the location of a .txt file
    print(f.read())
    f.close()

plateNum = str(input("Input plate number: \n"))
if plateNum == 'recordr':
    ReadRecord()
else:
    plateNumBool = CheckingValidPlate(plateNum)
    if plateNumBool == True:
        time = float(input("Input time(s): \n"))
        speed = SpeedCalculator(time)
        if speed <= 70:
            speedBool = False
            print("Within the speed limit")
            Recorder()
        else:
            speedBool = True
            print("Speeding")
            Recorder()
    else:
        print("Character must follow these guildlines: XX123XX")