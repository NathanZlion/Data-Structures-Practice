class Queue:
    def __init__(self):
        self.list = []
    
    def isempty(self):
        return len(self.list) == 0
        
    def enqueue(self, data):
        newlist = []
        newlist.append(data)

        # O(n) time complexity and space complexity
        for i in self.list:
            newlist.append(i)
        self.list = newlist        

    def dequeue(self):
        # done in O(1) time
        return self.list.pop()

    def getsize(self):
        return len(self.list)

    def __str__(self):
        if self.getsize()==0: return "EMPTY!"
        output = "[ "
        for i in range(len(self.list) -1):
            output += str(self.list[i] ) + ", "
        output += str(self.list[-1]) + " ]"
        return output
