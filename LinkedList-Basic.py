class linkedListNode():
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode
#"3"-->"7"-->"10"

#creating three unlinked nodes/objects
node1=linkedListNode("3")
node2=linkedListNode("7")
node3=linkedListNode("10")

#linking the nodes
node1.nextNode=node2 # node1-->node2  3-->7
node2.nextNode=node3 #node2-->node3   7-->10

currentNode=node1 #node1 is the head
while True:
    print(currentNode.value,end="-->")
    if currentNode.nextNode is None:
        print ("None")
        break
    currentNode=currentNode.nextNode #node increment/update