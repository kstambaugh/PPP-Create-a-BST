#Part 1: Create a BSTNode class

class BSTNode:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right
  def __str__(self):
    return str(self.data)
  def __repr__(self):
    return str(self.data)


#Part 2: Create a BST class

class BST:
  def __init__(self, root=None):
    self.root = root
    self.contents = []
  def __str__(self) -> str:
    if self.root == None:
      return "the tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output
  def __repr__(self) -> str:
    if self.root == None:
      return "the tree is empty"
  
  
  #Part 3: Add functionality to your BST class
  def add(self,node):
    if type(node) != int and type(node) != BSTNode:
      raise ValueError("You must pass an int or a BSTNode")

    if type(node) == int:
      node = BSTNode(node)

    if node.data in self.contents:
      return

    if self.root == None:
      self.root = node
      self.contents.append(node.data)
      return

    self.add_node(self.root, node)

  def add_node(self, cur_node, new_node):
    if new_node.data > cur_node.data:
      if cur_node.right == None:
        cur_node.right = new_node
        self.contents.append(new_node.data)
        return
      else:
        self.add_node(cur_node.right, new_node)
    else:
      if cur_node.left == None:
        cur_node.left = new_node
        self.contents.append(new_node.data)
        return
      else:
        self.add_node(cur_node.left, new_node)
