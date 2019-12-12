from computer import Computer

if(__name__ == "__main__"):
    with open("inputs.data", "r") as fs:
        commandArray = map(lambda x: int(x), fs.read().split(","))
        commandArray = list(commandArray)
        computer = Computer(commandArray, 0)
        elements = computer.next()
        while(elements):
            elements = computer.next()
