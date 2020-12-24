# Python program to insert element in binary tree 
class Tree():

  class newNode(): 

    def __init__(self, data): 
      self.key = data
      self.left = None
      self.right = None
  

  def __init__(self):
    self.root = None
      
  """ Inorder traversal of a binary tree"""
  def print_tree(self):
      self.inorder(self.root)

  def inorder(self,temp):
    if (not temp):
      return

    self.inorder(temp.left) 
    print(temp.key)
    self.inorder(temp.right) 


  """function to insert element in binary tree """
  def insert(self,temp, key):
    temp = self.root
    if self.root is None:
        pass
      #print("root actual", self.root)
    else:
        pass
       #print("root actual", self.root)
    if self.root is None:
      self.root = self.newNode(key)
      #print("root", self.root.key)
      return
    q = [] 
    q.append(temp) 

    # Do level order traversal until we find 
    # an empty place. 
    while (len(q)): 
      temp = q[0] 
      q.pop(0) 

      if (not temp.left):
        temp.left = self.newNode(key) 
        break
      else:
        q.append(temp.left) 

      if (not temp.right):
        temp.right = self.newNode(key) 
        break
      else:
        q.append(temp.right) 

  # A function to do preorder tree traversal 
  def Preorder(self, root, recorrido):
      
      if root: 
    
          # First print the data of node 
          recorrido.append(root.key) 
    
          # Then recur on left child 
          self.Preorder(root.left, recorrido) 
    
          # Finally recur on right child 
          self.Preorder(root.right, recorrido)
       
           
      return recorrido

    
  # Iterative Method to print the 
  # height of a binary tree
  def LevelOrder(self,root):
      # Base Case
      recorrido = []
      if root is None:
          return recorrido
      
      # Create an empty queue 
      # for level order traversal
      queue = []
  
      # Enqueue Root and initialize height
      queue.append(root)
  
      while(len(queue) > 0):
        
          # Print front of queue and 
          # remove it from queue
          #print (queue[0].key)
          recorrido.append(queue[0].key)
          node = queue.pop(0)
  
          #Enqueue left child
          if node.left is not None:
              queue.append(node.left)
  
          # Enqueue right child
          if node.right is not None:
              queue.append(node.right)
              
      return recorrido
  
