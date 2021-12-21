#using library functions
from collections import deque
arr=["Eren","Mikasa","Armin","Annie"]
queue=deque(arr)
queue.append("Jean") #enqueue
queue.popleft() #dequeue

#with class
class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)