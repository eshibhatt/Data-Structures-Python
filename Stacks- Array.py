#FILO= First In Last Out / LIFO= Last In First out
#   Push/Pop happens in only one side, i.e the end of stack

class Stack:
  def __init__(self):
    self.arr = [] #the data in stack class is held in arrays
    self.length = 0 #initial length
  
  def __str__(self):
    return str(self.__dict__)
  
  #to peek the last element
  def peek(self):
    top=self.length-1 #keeps track of the last element, where operations happen
    return self.arr[top]
  
  #to push in the end
  def push(self,value):
    self.arr.append(value)
    self.length += 1
  
  #to pop from the end
  def pop(self):
    top=self.length-1
    popped_item = self.arr[top]
    del self.arr[top]
    self.length -= 1
    return popped_item

  #to display entire stack
  def display(self):
    top=self.length-1
    a=0
    for a in range(0,top):
        print(self.arr[a])
        a+=1


mystack=Stack()

mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')

#to view the full stack
print(mystack)
mystack.display

x=mystack.peek() #storing return value of peek
print(x) #printing peek

mystack.pop()
print(mystack)

mystack.display