class Node():
    def _init_(self, data):
        self.data = data
        self.nextNode = None

class LinkedList():
    def _init_(self):
        self.head = None
        self.size = 0
    
    # 0(1)  !!!

    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode  = self.head
            self.head = newNode
    # 0(1)
    def size(self):
        return self.size
    # 0(N) not good
    def size(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size +=1
            actualNode = actualNode.nextNode

        return size

    def insertEnd(self, data):
        self.size = self.size +1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode= actualNode.nextNode

        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d " & actualNode.data)
            actualNode = actualNode.nextNode



