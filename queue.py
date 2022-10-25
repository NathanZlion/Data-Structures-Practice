class Queue:
    def __init__(self):
        self.list = []

    def isempty(self):
        return len(self.list) == 0

    def enqueue(self, data):
        self.list.insert(0, data)

    def dequeue(self):
        # done in O(1) time
        return self.list.pop()
    
    def peekNextInLine(self):
        return self.list[-1]

    def getsize(self):
        return len(self.list)

    def __str__(self):
        if self.getsize()==0: return "EMPTY!"
        output = "[ "
        for i in range(len(self.list) -1):
            output += str(self.list[i] ) + ", "
        output += str(self.list[-1]) + " ]"
        return output
