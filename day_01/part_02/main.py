import math

def calculate(fuel):
    calculatedFuel = math.floor(fuel / 3) - 2
    if(calculatedFuel > 0):
        return calculatedFuel + calculate(calculatedFuel)
    return 0

if(__name__ == "__main__"):
    with open("inputs.data", "r") as fs:
        sum = 0
        line = fs.readline()

        while line:
            sum += calculate(int(line)) 
            line = fs.readline()

        print("Calculated sum: {0}".format(sum))
