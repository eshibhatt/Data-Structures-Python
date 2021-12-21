class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #address of the next element
        self.prev = None #address of the previous element

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node #assigning the new node to the next of the current tail
            new_node.prev = self.tail #the current tail becomes the prev of new node
            self.tail = new_node #and the new node officially becomes tail
            self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head #the next of the new nod points to the node at current head
        self.head.prev = new_node #new node becomes the element before the current head
        #(the prev of head is none, till reassigned in which case the head changes too)
        self.head = new_node #the new node becomes the head
        self.length += 1

    def insert(self,index,data):
        new_node = Node(data)
        if index==0:
            self.prepend(data)
            return
        if index >= self.length:
            self.append(data)
            return
        else:
            #element right before the new node 
            leader = self.traversetoindex(index - 1)
            #element right after the new node
            follower = leader.next
            #new node goes right in between leader and follower
            leader.next = new_node
            new_node.next = follower
            new_node.prev = leader
            follower.prev = new_node
            self.length+=1

    def remove(self,index):
        if index==0:
            self.head=self.head.next
            self.length-=1
            return
        if index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        leader = self.traversetoindex(index-1)
        unwanted_node = leader.next
        holder = unwanted_node.next
        leader.next = holder
        holder.prev = leader
        self.length -= 1


    def traversetoindex(self,index):
        curr_node = self.head
        i = 0
        while i!= index:
            curr_node = curr_node.next
            i+=1
        return curr_node

    def printt(self):
        temp = self.head
        while temp != None:
            print(temp.data , end = ' ')
            temp = temp.next
        print()
        print('Length ' + str(self.length))        
            
        
d = DoublyLinkedList()
d.append(10)
d.append(5)
d.append(6)
d.prepend(1)
d.insert(2,22)
d.remove(3)
d.printt()