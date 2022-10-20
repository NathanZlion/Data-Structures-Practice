

class Node:
    def __init__(self, data, next= None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self, data):
        node = Node(data)
        self.head = node
        self.tail = node
        self.tail.next = self.head
        self.length = 1

    def addLast(self, data):     # Time Complexity: O(1)
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
        self.length +=1

    def addFirst(self, data):   # Time Complexity: O(1)
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head
        self.length += 1

    def addAtIndex(self, data, index):  # Time Complexity: O(n)
        assert index <= self.length, ">>> !!! Warning index out of range"
        while index<0:
            index += self.length
        if self.isEmpty():return self.addFirst(data)
        if index==0:return self.addFirst(data)
        if index==self.length-1: return self.addLast(data)
        newNode = Node(data)
        currIndex = 1
        currNode = self.head
        while currIndex <index:
            currNode = currNode.next
            currIndex +=1
        nextNode =currNode.next
        currNode.next = newNode
        newNode.next = nextNode
        self.length+=1

    def removeLast(self): # Time Complexity: O(n)
        if self.isEmpty():
            print("Empty Linked List.")
            return None
        elif self.length == 1:
            res=self.head.data
            self.head = None
            self.tail = None
            self.length -=1
            return res
        currNode=self.head
        while not(currNode.next is self.tail):
            currNode=currNode.next
        currNode.next=self.head
        res=self.tail
        self.tail=currNode
        self.length-=1
        return res.data

    def removeFront(self):  # Time Complexity: O(1)
        if self.isEmpty():
            print("Empty Linked List.")
            return None
        res = self.head.data
        if self.length==1:
            self.head=None
            self.length-=1
            return res
        self.head=self.head.next
        self.tail.next=self.head
        self.length-=1
        return res

    def removeAtIndex(self, index):     # Time Complexity: O(n)
        if self.isEmpty():
            print("Empty Linked List.")
            return None
        assert index<self.length, "Index out of range"
        if self.length==1: return self.removeFront()
        if index==0:return self.removeFront()
        if index==self.length-1: return self.removeLast()

        # Handling negative indexing as an indexing from the right to left
        while index<0:
            index+=self.length

        currIndex=0
        currNode=self.head
        while currIndex<index-1:
            currNode=currNode.next
            currIndex+=1

        res = currNode.next.data
        currNode.next=currNode.next.next
        self.length-=1
        return res

    def isEmpty(self):    # Time Complexity: O(1)
        return self.length == 0

    def printIt(self):      # Time Complexity: O(n)
        if not self.head: 
            print("Empty Linked List.")
            return
        print("_____________________\nCircular Linked List")
        currNode = self.head
        while not(currNode.next is self.head):
            print(str(currNode.data), end=" > ")
            currNode = currNode.next
        print(str(currNode.data))
        print("- - - - - - - - - - -")


cir = CircularLinkedList(9)

cir.printIt()
print(cir.removeAtIndex(-1))
cir.printIt()