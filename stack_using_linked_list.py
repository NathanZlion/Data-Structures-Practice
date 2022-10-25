


# Singly Linked List 
# Implemented for use in building a stack

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):return self.length == 0    # Time Complexity: O(1)
    
    def pushAtFront(self, data):    # time complexity O(1)  pushes at the front
        newNode = Node(data)
        if self.isEmpty(): self.head= self.tail= newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
    
    def popAtFront(self):
        if self.head is None: return None
        else:
            temp = self.head
            self.length -=1
            if self.length ==0:
                self.head = self.tail= None
                return temp.data
            self.head = self.head.next
            return temp.data

    def getLength(self): return self.length

    def getList(self):
        return self.__str__()

    def __str__(self):
        currNode = self.head
        output = "\n\n"
        while not(currNode == None):
            output += ("\t|_ " +str(currNode.data)+'\n')
            currNode = currNode.next
        return output


class Stack:
    def __init__(self):
        self.stack = linkedList()
    
    def push(self, data):
        self.stack.pushAtFront(data)
    
    def pop(self):
        return self.stack.popAtFront()

    def getLength(self):
        return self.stack.getLength()
    
    def isEmpty(self):
        return self.stack.isEmpty()
    
    def __str__(self):
        return self.stack.getList()

myStack = Stack()

myStack.push("youtube")
myStack.push("facebook")
myStack.push("instagram")
myStack.push("tiktok")
myStack.push("upwork")

print(myStack)
