class Computer:
    position = 0
    nextStep = 0
    resultPosition = 0

    def __init__(self, commandArray, resultPosition):
        self.data = commandArray
        self.resultPosition = resultPosition

    def addition(self):
        self.data[self.data[self.position + 3]] = self.data[self.data[self.position + 1]] + self.data[self.data[self.position + 2]]
        self.nextStep = 4
        return self.data

    def multiplication(self):
        self.data[self.data[self.position + 3]] = self.data[self.data[self.position + 1]] * self.data[self.data[self.position + 2]]
        self.nextStep = 4
        return self.data

    def close_computer(self):
        print("Result:")
        print(self.data[self.resultPosition])
        print("Done with execution!")
        return False

    commands = {
        1: addition,
        2: multiplication,
        99: close_computer
    }

    def next(self):
        self.position = self.nextStep + self.position
        command = self.data[self.position]
        return self.commands[command](self)
        
