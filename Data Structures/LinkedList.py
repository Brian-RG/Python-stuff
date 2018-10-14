import Node
class LinkedList:
    def __init__(self,Node):
        self.head=self.final=Node
    def add(self,Node):
        current=self.head
        while(current.getNext()!=None):
            current=current.getNext()
        current.setNext(Node)
        self.final=Node
    def write(self):
        print(self.head,end="")
        c=self.head.getNext()
        while(c!=None):
            print("-->",end="")
            print(c,end="")
            c=c.getNext()
        print()

a=Node.Node(4)
l=LinkedList(a)
l.add(Node.Node(7))
l.add(Node.Node(9))
l.add(Node.Node(10))
l.add(Node.Node(2))
l.add(Node.Node(3))
l.write()