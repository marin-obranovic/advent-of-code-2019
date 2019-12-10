from enum import Enum

def addition(startingIndex, commandArray):
    commandArray[commandArray[startingIndex + 3]] =  commandArray[commandArray[startingIndex + 1]] + commandArray[commandArray[startingIndex + 2]]
    return commandArray

def multiplication(startingIndex, commandArray):
    commandArray[commandArray[startingIndex + 3]] =  commandArray[commandArray[startingIndex + 1]] * commandArray[commandArray[startingIndex + 2]]
    return commandArray

if(__name__ == "__main__"):
    with open("inputs.data", "r") as fs:
        commandArray = map(lambda x: int(x), fs.read().split(","))
        commandArray = list(commandArray)
        element = commandArray[0]
        position = 0    
        while(element):
            if(element == 1):
                commandArray = addition(position, commandArray)
                position += 3
            elif(element == 2):
                commandArray = multiplication(position, commandArray)
                position += 3
            elif(element == 99):
                print("Hit 99 -> exiting")
                print(commandArray)
                break

            position += 1
            if(position == len(commandArray)):
                print(commandArray)
                break
            element = commandArray[position]
