class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    def getval(self):
        return self.value
    def setval(self, nval):
        self.value=nval
    def getNext(self):
        return self.next
    def setNext(self,n):
        self.next=n
    def __str__(self):
        return str(self.value)
    
if __name__ == "__main__":
    a=Node(5)