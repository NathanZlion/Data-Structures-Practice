

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self):
        self.head= None
        self.tail = None
        self.length = 0
    
    def push(self,data):     # Time Complexity: O(1)
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length +=1
    
    def pushAtIndex(self, data, index):     # Time Complexity: O(n)
        if index >= self.length:
            return self.push(data)

        newNode = Node(data)
        if index == 0:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            return None
        if index < 0:
            factor = (index*(-1)) // self.length
            index += ((self.length) * (factor+1))
            index +=1
            return self.pushAtIndex(data, index)

        currIndex = 0
        currNode = self.head
        while currIndex < index:
            currNode = currNode.next
            currIndex += 1

        prevNode = currNode.prev
        currNode.prev = newNode
        newNode.next = currNode
        prevNode.next = newNode
        newNode.prev = prevNode

        self.length += 1

    def pop(self):          # Time Complexity: O(1)
        if not self.head:
            return "! Empty Doubly Linked List"
        elif self.length == 1:
            poppedData = self.head.data
            self.head = None
            self.tail = None
            self.length -= 1
            return poppedData

        self.tail = self.tail.prev
        poppedData = self.tail.next.data
        self.tail.next = None
        self.length -= 1
        return poppedData
    
    def popAtIndex(self, index):    # Time Complexity: O(n)
        if not self.head:
            return "! Empty Doubly Linked List"

        if index >= self.length-1:
            return self.pop()

        if index < 0:
            factor = (index*(-1)) // self.length
            index += ((self.length) * (factor+1))
            return self.popAtIndex(index)
        
        if index == 0:
            poppedNode = self.head
            poppedData = poppedNode.data
            poppedNode = None
            self.head = self.head.next
            self.head.prev = Node
            self.length -= 1
            return poppedData
        
        currNode = self.head
        currIndex = 0
        while currIndex < index:
            currIndex +=1
            currNode = currNode.next
        prevNode = currNode.prev
        nextNode = currNode.next
        poppedData = currNode.data
        prevNode.next = nextNode
        nextNode.prev = prevNode
        currNode = None

        self.length -= 1
        return poppedData

    def peek(self):    # Time Complexity: O(1)
        if self.isEmpty():
            return "! Empty Doubly Linked List"
        return self.tail.data
    
    def peekAtIndex(self, index):   # Time Complexity: O(n)
        if index >= self.length:
            return self.peek()
        if index < 0:
            factor = (index*(-1)) // self.length
            index += ((self.length) * (factor+1))
            return self.peekAtIndex(index)
        
        currNode = self.head
        currIndex = 0

        while currIndex < index:
            currNode = currNode.next
            currIndex +=1
        return currNode.data

    def isEmpty(self):
        return self.length == 0

    def __str__(self):
        if not self.head:
            return "! Empty Doubly Linked List"
        
        currNode = self.head
        res = ""
        while currNode:
            res += str(currNode.data) + (" ~ ")
            currNode = currNode.next
        return res + "null"


myDL = doublyLinkedList()
myDL.push(0)
myDL.push(1)
myDL.push(2)
myDL.push(3)
myDL.push(4)
myDL.pushAtIndex(5, -1)

print(myDL.peekAtIndex(-4))
print(myDL)