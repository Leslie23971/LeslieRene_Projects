


class Node:
    # Constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    # Constructor
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)

        if self.head :
            current = self.head
            while current.next :
                current = current.next
            current.next = newNode
        else :
            self.head = newNode
    
    def search(self, target):
        listTail = self.head
        while listTail != None :
            if target == listTail.data :
                return listTail
            else :
                listTail = listTail.next
        return None
    
    def updateHead(self,data):
        newNode = Node(data)

        # Update the new nodes next val to existing node
        newNode.next = self.head
        self.head = newNode
    
    def removeNode(self,data):
        if self.head :
            if data == self.head.data :
                if (self.head.next) :
                    self.head = self.head.next
                else :
                    self.head = None
                return
            
            previous = self.head
            current = self.head.next

            while (current) :
                if data == current.data :
                    if (current.next) :
                        previous.next = current.next
                    else :
                        previous.next = None
                previous = current
                current = current.next

    
    def printlist(self):
      printval = self.head
      while printval:
        print (printval.data)
        printval = printval.next


# Create Linked list
print("***** Create Linked list ***** ")
lkdList = Linkedlist()

# Init Linked list
print("***** Init linked list ***** ")
lkdList.head = Node(4)
lkdList.printlist()

# Insert nodes
print("***** Insert Nodes ***** ")
lkdList.insert(9)
lkdList.insert(52)
lkdList.insert(5)
lkdList.insert(490)
lkdList.insert(2)
lkdList.insert(3)
lkdList.insert(2)
lkdList.insert(58)
lkdList.insert(52)

# Print List
lkdList.printlist()

# Search Nodes
print("***** Search Nodes ***** ")
print("52 NOT found !!" if lkdList.search(52) == None else "52 Node FOUND in linked list")
print("38 NOT found !!" if lkdList.search(38) == None else "38 Node FOUND in linked list")
print("4 NOT found !!" if lkdList.search(4) == None else "4 Node FOUND in linked list")
print("7 NOT found !!" if lkdList.search(7) == None else "7 Node FOUND in linked list")
print("58 NOT found !!" if lkdList.search(58) == None else "58 Node FOUND in linked list")

# Remove Nodes
print("***** Remove Nodes ***** ")
lkdList.removeNode(2)
lkdList.removeNode(52)
lkdList.removeNode(60)
lkdList.printlist()

# Update head
print("***** Update head ***** ")
lkdList.updateHead(22)
lkdList.printlist()