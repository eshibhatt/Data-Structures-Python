class Node():

  def __init__(self,value):
    self.value = value
    self.next = None
    
class LinkedList():
  #constructor
  def __init__(self):
    #the attributes below are merely pointers, not the 1st and last node itself
    self.head = None #stores the address of the first node
    self.tail = None #stores the address of the last node
  
  #insert at end - O(1)
  def append(self,data):
    #1st we create a new node by passing new_element as value to Node class
    new_node = Node(data)
    if self.head == None:
      self.head = new_node #we assign the head to the new node, from none
      self.tail = self.head #as its of length 1, the head and tail refer to the same node
      self.length = 1
    else:
      self.tail.next = new_node #pointing the next of the node of the current tail to the new node(from none)
      #now we have a new node, which is the last item
      self.tail = new_node  #so we update the tail, to the new node
      self.length += 1

  #insert at beginning - O(1)
  def prepend(self,data):
    new_node = Node(data)
    new_node.next = self.head #making the new node's next, point to the node which is the current head
    self.head = new_node #reassigning the head, to the new node
    self.length += 1

  #insert at desired position - O(n)   
  '''
                LOGIC     *--* ==> *--*  ==> *    * ==> *--*--*
                                  /        \  /
                             *       *          *         x  
                new_node.nextNode =currentNode.nextNode #the new node points where the current node was pointing
                currentNode.nextNode=new_node #the currentNode updates to point to the new_node currentNode=self.head '''
  def insert(self,index,data):
    new_node = Node(data)
    i = 0
    currentNode= self.head
    #1st we check the parameters
    if index>=self.length:
      #you can either give an error or just add it to the tail
      self.append(data)
      return 
    if index ==0:
      self.prepend(data)
      return
    while i<self.length:
      if i == index-1: # we are changing the pointers of the element right before the desired position
        currentNode.next , new_node.next = new_node , currentNode.next #points two steps after
        self.length+=1
        break
      currentNode = currentNode.next
      i+=1
    
  #removing an element in position - O(n)
    ''' LOGIC      *   * ==> *--*  ==> *--*
                    \ /           
                     *        *              
    
    as soon as the reference to the node is destroyed,
    the node is deleted too'''
  def remove(self,index):
    currentNode = self.head
    i=0
    if index>=self.length:
      print("Entered wrong index")
    
    if index == 0:
      self.head = self.head.next #reassigning the head to the 2nd element
      self.length -= 1   
      return       

    while i<self.length:
      if i == index-1:
        currentNode.next = currentNode.next.next
        self.length-=1
        break
      i+=1
      currentNode = currentNode.next

  #printing the linkedList - O(n)
  def printl(self):
    currentNode= self.head
    while currentNode!= None:
      print(currentNode.value , end = ' ')
      currentNode = currentNode.next
    print()
    print('Length = '+str(self.length))
  
  #Reverse Printing the linkedList (Recursive)
  def reversePrint(self):
    if self.head==None:
        return
    else:
        reversePrint(self.head.next)
        print(self.head.data)

  # Reversing the linkedList - O(n)
  def reverse(self):
    if self.length==1:
      return self.head
    prev = None #holds the address of the prev elements/iterated before; initialised at none as 1st element has no prev
    self.tail = self.head #reassigning the tail tail attribute to the address of the 1st node
    while self.head != None:
      currentNode= self.head
      self.head = self.head.next #passing the head attribute till it reaches the last node
      #changing the next of the currentNode to point to the address of the element iterated before
      currentNode.next = prev #making the next of the current node, to point to the prev
      prev = currentNode #updating the address in prev to address of the currentNode, which will be the prev to the next iteration of currentNode
    self.head = currentNode

l = LinkedList()
l.append(10)
l.append(5)
l.append(6)
l.prepend(1)
l.insert(2,99)
l.insert(34,23)
l.remove(5)
l.reverse()
l.printl()
print(l.head.value, l.tail.value)
