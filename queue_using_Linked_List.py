


# Singly Linked List 
# Implemented for use in building a queue

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

    def push(self, data):               # Time Complexity: O(1)  push at end
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1
    
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

    def peek(self):                          # Time Complexity: O(1)
        if self.isEmpty():
            return ("! Empty Linked List")
        return self.tail.data
    
    def getLength(self): return self.length

    def getList(self):
        return self.__str__()

    def __str__(self):
        currNode = self.head
        output = " "
        while not(currNode == None):
            output += ("< " +str(currNode.data)+" -")
            currNode = currNode.next
        return output

class Queue:
    def __init__(self):self.queue = linkedList()
    
    def enque(self, data): self.queue.push(data)
    
    def dequeue(self): return self.queue.popAtFront()
    
    def isEmpty(self): return self.queue.isEmpty()
    
    def getLength(self): return self.queue.getLength()
    
    def __str__(self): return self.queue.getList()


myQue = Queue()


myQue.enque(1)
myQue.enque(2)
myQue.enque(3)
myQue.enque(4)

print(myQue)
print(myQue.dequeue())
print(myQue)
myQue.enque(5)
print(myQue.dequeue())
print(myQue)
print(myQue.dequeue())
print(myQue)
print(myQue.dequeue())
print(myQue)
