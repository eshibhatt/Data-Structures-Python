class Node:
  def __init__(self,data):
    self.data = data 
    self.left = None #pointer to lower value
    self.right = None #pointer to higher value

class BinarySearchTree:
  def __init__(self):
    self.root = None

  #inserting
  def insert(self,data):
    new_node = Node(data)

    #if the tree is empty and has no root node
    if self.root == None:
      self.root = new_node
      return
    else:
      curr_node = self.root
      #we will traverse till we find the right place to insert
      while True:
        if data < curr_node.data:
          #Left
          if curr_node.left == None: #no node next
            curr_node.left = new_node
            #as soon as we hit a pointer to None we operate on it
            #and exit the loop by return, or else it will go infinite
            return 
          else:
            curr_node = curr_node.left #step increment till we reach the end
        
        elif data > curr_node.data:
            #Right
            if curr_node.right == None:
              curr_node.right = new_node
              return
            else:
              curr_node = curr_node.right

  #the search/lookup function, to check it an item exists in the BST
  def lookup(self,data):
    curr_node = self.root
    while True:
      if curr_node == None: #reaches end without finding it
        return False
      if curr_node.data == data: #it finds it
        return True
      elif data < curr_node.data: #traverse to left
        curr_node = curr_node.left
      else: #traverse to right
        curr_node = curr_node.right
    
  

  #Inorder Traversal (We get sorted order of elements in tree)
  def print_tree(self):
    if self.root != None:
      self.printt(self.root)
    
  def printt(self,curr_node):
    if curr_node != None:
      self.printt(curr_node.left)
      print(str(curr_node.data))
      self.printt(curr_node.right)


  #code to remove a value from the BST
  def remove(self,data):
      if self.root == None:
          return False

      currentNode = self.root
      parentNode = None

      while currentNode:
          #traverse till we find a match
          if data < currentNode.data: #left
              parentNode = currentNode
              currentNode = currentNode.left
          elif data > currentNode.data:#right
              parentNode = currentNode
              currentNode = currentNode.right

          # We have a match, lets get to work!
          elif data == currentNode.data:
              # Option 1: Match has No right child:
              #we keep a ref to the parent node, and replace the current with its 1st left child
              if currentNode.right == None:
                  if parentNode == None: #it is the root variable, we will remove
                      self.root = currentNode.left
                  else:
                      #if parent > current data, make current left child a child of parent
                      if currentNode.data < parentNode.data:
                          parentNode.left = currentNode.left
                      #if parent < current data, make left child a right child of parent
                      elif currentNode.data > parentNode.data:
                          parentNode.right = currentNode.left

              #Option 2: Right child which doesnt have a left child
              elif currentNode.right.left == None:
                  currentNode.right.left = currentNode.left
                  if parentNode == None:
                      self.root = currentNode.right
                  else:
                      #if parent > current, make right child of the left the parent
                      if currentNode.data < parentNode.data:
                          parentNode.left = currentNode.right
                      #if parent < current, make right child a right child of the parent
                      elif currentNode.data > parentNode.data:
                          parentNode.right = currentNode.right


              #Option 3: Right child that has a left child
              else:
                  #find the Right child's left most child
                  leftmost = currentNode.right.left
                  leftmostParent = currentNode.right
                  while leftmost.left != None:
                      leftmostParent = leftmost
                      leftmost = leftmost.left

                  #Parent's left subtree is now leftmost's right subtree
                  leftmostParent.left = leftmost.right
                  leftmost.left = currentNode.left
                  leftmost.right = currentNode.right

                  if parentNode == None:
                      self.root = leftmost
                  else:
                      if currentNode.data < parentNode.data:
                          parentNode.left = leftmost
                      elif currentNode.data > parentNode.data:
                          parentNode.right = leftmost
          return True

        

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)

x = bst.lookup(6) #true
print(x)
y = bst.lookup(99) #false
print(y)
bst.print_tree() #prints in sorted