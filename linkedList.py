

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):                  # Time Complexity: O(1)
        return self.length == 0

    def push(self, data):               # Time Complexity: O(1)
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        elif self.length == 1:
            self.head.next = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1

    def pushAtIndex(self, data, index):   # Time Complexity: O(n)
        if index >= self.length:
            self.push(data)
            return

        if index < 0:
            factor = (index*(-1)) // self.length
            index += ((self.length) * (factor + 1))

        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return 
    
        currNode = self.head
        currIndex = 0
        while currIndex <= index-2:
            currIndex +=1
            currNode = currNode.next

        laterNode = currNode.next
        currNode.next = newNode
        newNode.next = laterNode
        self.length += 1

    def pop(self):                 # Time Complexity: O(n)
        currNode = self.head
        if self.isEmpty():
            return "! Empty Linked List"

        elif self.length == 1:
            data = self.head.data
            self.head.next = None
            self.head = None
            self.tail = self.head
            self.length -=1
            return data

        while currNode.next:
            if currNode.next == self.tail:
                break
            currNode = currNode.next
        self.tail = currNode
        poppedNode = currNode.next
        currNode.next = None
        self.length -= 1

        return poppedNode.data

    def popAtIndex(self, index):             # Time Complexity: O(n)
        if index == 0:
            poppedData = self.head.data
            self.head = self.head.next
            return poppedData

        if index < 0:
            factor = (index*(-1)) // self.length
            index += ((self.length) * (factor + 1))
    
        if index >= self.length-3:
            return self.pop()

        currIndex = 1
        currNode = self.head
        while currIndex <index:
            currNode = currNode.next
        currNode.next = currNode.next.next
        
        return currNode.data

    def peek(self):                          # Time Complexity: O(1)
        if self.isEmpty():
            return ("! Empty Linked List")
        return self.tail.data
    
    def peekAtIndex(self, index):            # Time Complexity: O(n)
        if self.isEmpty():
            return "! Empty Linked List"

        if index > self.length:
            return "! index Out of range"
        
        if index == self.length -1:
            return self.peek()
        
        if index < 0:
            while index <0:
                index += self.length
        
        currNode = self.head
        currIndex = 0
        while currIndex < index:
            currNode = currNode.next
            currIndex += 1
        return currNode.data

    def __str__(self):
        currNode = self.head
        output = ""
        while not(currNode == None):
            output += (str(currNode.data) + ' -> ')
            currNode = currNode.next
        return (output + "null")

myL = linkedList()
myL.push(0)
# myL.push(1)
# myL.push(2)
# myL.push(3)
# myL.push(5)
# myL.pushAtIndex("four", 4)
# print(myL.head.data)
# print(myL.popAtIndex(-1))
# myL.pop()
# myL.pop()
# myL.pop()
# print(myL.peek())
# print(myL.peekAtIndex(2))


print(myL)