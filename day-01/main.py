import math

if(__name__ == "__main__"):
    with open("inputs.data", "r") as fs:
        sum = 0
        line = fs.readline()

        while line:
            sum += math.floor(int(line) / 3) - 2 
            line = fs.readline()

        print("Calculated sum: {0}".format(sum))
