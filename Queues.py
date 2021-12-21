#FIFO- First in First out
# enqueue happens in the end, dequeue happens in the beginning

class Node:
  def __init__(self,val):
    self.val = val
    self.next = None

class Queue:
  def __init__(self):
    self.first = None #keeps track of where we remove
    self.last = None #keeps track of where we add
    self.length = 0 
  
  def is_empty(self):
    if self.length==0:
      return True
    else:
      return False

  #to view the element at top, ie the 1st element
  def peek(self):
    return self.first.val
  
  def enqueue(self,val):
    new_node = Node(val)
    
    if self.first == None: #if length is 0
      self.first = new_node
      self.last = self.first #since there only 1 element
      self.length += 1
    else:
      self.last.next = new_node #pointing the next of the current last, to the new node
      self.last = new_node #updating the last
      self.length += 1
  
  def dequeue(self):
    temp = self.first.next #tracking the 2nd element, which will be the next top after dequeue
    dequeued_element = self.first #the element to be dequed
    
    if self.is_empty is True:
      return "underflow"
    elif temp == None: #only one element
      self.first = None
      self.length -= 1
      return
    # as removing the reference of a node deletes it
    self.first.next = None #we remove the reference link at the next of the 1st node
    self.first = temp #assigning top to the 2nd element
    self.length -= 1

  def display(self):
    temp = self.first
    while temp != None:
      print(temp.val , end = '->')
      temp = temp.next
    print()
    print(self.length)

myq = Queue()
myq.enqueue('google')
myq.enqueue('microsoft')
myq.enqueue('facebook')
myq.enqueue('apple')
myq.display()
myq.dequeue() #removes 'google' which is at top
myq.display()
x = myq.peek()
print(x)