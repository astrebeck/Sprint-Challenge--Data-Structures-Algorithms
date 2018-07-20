class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    node_start = self
    cb(node_start.value)
    node = node_start.left
    rights = []
    lefts = []
    
    while(node):

      cb(node.value)

      if(node.right):

        rights.append(node.right)

      node = node.left

    for obj in rights:

      cb(obj.value)

    node = node_start
    node = node.right

    while(node):

      cb(node.value)

      if(node.left):
        lefts.append

      node = node.right

    for obj in lefts:

      cb(node.value)




  def breadth_first_for_each(self, cb):
    node = self
    nodes = [node]

    for obj in nodes:

      if not obj.left in nodes and obj.left != None:
        nodes.append(obj.left)

      if not obj.right in nodes and obj.right != None:
        nodes.append(obj.right)

    for obj in nodes:

      cb(obj.value)

    print(nodes)




  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
