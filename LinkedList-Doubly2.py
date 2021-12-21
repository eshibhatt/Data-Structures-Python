#doubly linkedlist
class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def append(self,element):
        newNode=node(element)
        if self.head==None:
            self.head=newNode
            self.tail=self.head
            self.length=1
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
            self.length+=1
    
    def prepend(self,element):
        newNode=node(element)
        if self.length==0:
            return self.append(element)
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
            self.length+=1
    
    def insert(self,index,element):
        newNode=node(element)
        if index>=self.length:
            self.append(element)
        elif index==0:
            self.prepend(element)
        
        i=0
        currentNode=self.head
        while i<self.length:
            if i==index-1:
                newNode.next=currentNode.next
                newNode.prev=currentNode
                currentNode.next=newNode
                self.length+=1
            currentNode=currentNode.next
            i+=1
    
    def remove(self,index):
        if index==0:
            self.head=self.head.next
            self.length-=1
        i=0
        currentNode=self.head
        while i<self.length:
            if i==index-1:
                currentNode.next=currentNode.next.next
                self.length-=1
                if currentNode.next!=None:
                    currentNode.next.prev=currentNode
                break
            currentNode=currentNode.next
            i+=1
    def printL(self):
        currentNode=self.head
        while currentNode!=None:
            print(currentNode.value,end="-->")
            currentNode=currentNode.next
        print()
        print("length="+str(self.length))

j=LinkedList()
j.append("jordan")
j.append("michael")
j.prepend("oliver")
j.printL()

j.insert(1,"rebekah")
j.printL()

j.remove(2)
j.printL()