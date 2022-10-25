

from random import choice

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self):
        self.root = None
        self.length = 0
        self.bracesMap = {"{":"}", "[":"]","<":">","(":")"}
        self.braces = ["{","[","<","("]

    def insert(self, value):
        newNode = Node(value)
        if not self.root: self.root=newNode
        else:
            parent = self.root
            child = self.root
            while not(child is None):
                parent = child
                if parent.value > newNode.value: child = parent.left
                else:child = parent.right
            if parent.value> value: parent.left = newNode
            else: parent.right = newNode
        self.length +=1
    
    def lookUp(self, value):        # time complexity : O(logn)
        if not self.root: return "this binary tree is empty"
        currnode = self.root
        res= "/"
        while currnode is not None:
            if currnode.value == value: return res+ str(currnode.value)
            elif currnode.value > value:
                res+=f" {currnode.value}> L:"
                currnode = currnode.left
            else:
                res+=f" {currnode.value}> R:"
                currnode = currnode.right

        return "result not Found, Lookup history >>> " +res+"NONE"

    def remove(self, value):
        if self.root.value == value: self.root = None
        parent = self.root
        child = self.root
        removed = False
        while (child is not None) and (not removed):
            if parent.value > value:
                child = parent.left
                dirn = "l"
            else:
                child = parent.right
                dirn ="r"
            if not(child is None) and child.value == value:
                if dirn == "l": parent.left= None
                else: parent.right = None
                return None
            parent = child
    

    def printIt(self, inputNode = "notGiven"):
        if inputNode == "notGiven": currNode =  self.root
        else: currNode = inputNode
        if currNode is None: return str("#")
        openingBrace = choice(self.braces)
        closingBrace = self.bracesMap[openingBrace]

        return f"({str(currNode.value)} {openingBrace} {self.printIt(currNode.left)} _ {self.printIt(currNode.right)} {closingBrace})"

myTree = binaryTree()
myTree.insert(500)
myTree.insert(134)
myTree.insert(34)

print(myTree.printIt())
