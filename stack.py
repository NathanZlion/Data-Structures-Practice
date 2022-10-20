class stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.list.pop()

    def peek(self):
        return self.list[-1]

    def getsize(self):
        return len(self.list)

    def __str__(self):
        output = "[ "
        for i in range(len(self.list)-1):
            output += str(self.list[i]) + ", "
        output += str(self.list[-1] )+ "]"
        return output
