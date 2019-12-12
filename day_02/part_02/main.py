from computer import Computer
import sys

if(__name__ == "__main__"):
    for x in range(99):
        for y in range(99):
            with open("inputs.data", "r") as fs:
                commandArray = map(lambda x: int(x), fs.read().split(","))
                commandArray = list(commandArray)
                commandArray[1] = x
                commandArray[2] = y
                computer = Computer(commandArray, 0)
                elements = computer.next()
                while(elements):
                    elements = computer.next()
                    if(elements and elements[0] == 19690720):
                        print("x = {0} and y = {1}".format(x, y))
                        sys.exit()
