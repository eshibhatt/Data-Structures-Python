class Node:
  def __init__(self,data):
    self.data = data
    self.prev = None

class Stack:
  def __init__(self):
    self.top = None
    self.length = 0
  
  #to see the top element
  def peek(self):
    return self.top.data

  #to add in the end
  def push(self,data):
    new_node = Node(data)

    if self.length == 0:
      self.top = new_node
      self.length = 1
    else:
      new_node.prev = self.top
      self.top = new_node
      self.length += 1

  #to delete from the end
  def pop(self):
    if not self.top:
      return None
    holderPointer = self.top #hold the value to be poped
    self.top = self.top.prev
    self.length -= 1
    return holderPointer.data #returns the poped value

  #to display whole stack
  def printt(self):
    current= self.top
    while current != None:
      print(current.data , end = ' -> ')
      current = current.prev #increment
    print()

mystack = Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
mystack.printt()

x = mystack.peek()
print(x)

y=mystack.pop()
print(y)

mystack.printt()

qw = mystack.peek()
print(qw)