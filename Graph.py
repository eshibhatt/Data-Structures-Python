#undirected unweighted graph

class Graph:

  def __init__(self):
    self.numberofnodes = 0 #keep track of the no of nodes
    self.adjacentlist = {} #using a hashtable to implement an adjacency list
    #storing as 'node':[connections], in key value pairs
  
  #helps provide a simple output of the data in the object
  def __str__(self):
    return str(self.__dict__)
  
  #adds a node
  def addVertex(self,node):
    #as the new node will not have links by default
    #we are adding the 'node':[] to our adjacency list
    self.adjacentlist[node] = [] 
    self.numberofnodes += 1
  
  #adds an undirected connection between node1 and node2
  def addEdge(self,node1,node2):
    #pushing the nodes in each other's adjacency list value
    self.adjacentlist[node1].append(node2) #it will push to the array of connections
    self.adjacentlist[node2].append(node1)
  
  #shows all the connections of the graphs we create (nodewise)
  def showconnection(self):
    for x in self.adjacentlist:
      print(x , end = '-->')
      for i in self.adjacentlist[x]:
        print(i , end = ' ') 
      print()

#declaring the graph
myGraph = Graph()
#adding nodes
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
#connecting nodes
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')
#displaying
print(myGraph)
myGraph.showconnection()