class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      # TODO complete Node initialization
      self.left = None
      self.right = None
      self.height = 0

  def __init__(self):
    self.__root = None
    # TODO complete initialization

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    if self.__root == None:
      self.__root = Binary_Search_Tree.__BST_Node(value)
      self.__root.height += 1
    else:
      self.__insert_rec(value, self.__root)
	  
  def __insert_rec(self, value, t):
    if value < t.value:
      if t.left == None:
        t.left = Binary_Search_Tree.__BST_Node(value)
        t.left.height = 1
        if t.right == None:
          t.height = t.left.height + 1
        else:
          t.height = max(t.left.height, t.right.height) + 1
      else:
        self.__insert_rec(value, t.left)
        if t.right == None:
          t.height = t.left.height + 1
        else:
          t.height = max(t.left.height, t.right.height) + 1 
		  

    elif value > t.value:
      if t.right == None:
        t.right = Binary_Search_Tree.__BST_Node(value)
        t.right.height = 1
        if t.left == None:
          t.height = t.right.height + 1
        else:
          t.height = max(t.left.height, t.right.height) + 1
      else:
        self.__insert_rec(value, t.right)
        if t.left == None:
          t.height = t.right.height + 1
        else:
          t.height = max(t.left.height, t.right.height) + 1    		  

	  
    else:
      raise ValueError
	  
  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    if self.__root is None:
      raise ValueError
    else:
      self.__remove_rec(value, self.__root)
	  
  def __min_val(self,t):
    if t.left == None:
      return t.value
    else:
      return self.__min_val(t.left)
	  
  def __remove_rec(self, value, t):
    if t == None:
      return t 
    if value == t.value:
      if t.left == None and t.right == None:
        #t.height = 0
        t = None
        self.root = None
        return t
      elif t.left == None:
        return t.right
      elif t.right == None:
        return t.left
    		
      else:
        a = self.__min_val(t.right)
        t.value = a
        t.right = self.__remove_rec(a, t.right)
        if t.left == None and t.right == None:
          t.height = 1
        elif t.left == None and t.right is not None:
          t.height = t.right.height - 1
        elif t.right == None and t.left is not None:
          t.height = t.left.height - 1
        else:
          t.height = max(t.left.height, t.right.height) - 1
      return t

    elif value < t.value:
      t.left = self.__remove_rec(value, t.left)
      if t.left == None and t.right == None:
        t.height = 1
      elif t.left == None and t.right is not None:
        t.height = t.right.height - 1
      elif t.right == None and t.left is not None:
        t.height = t.left.height - 1
      else:
        t.height = max(t.left.height, t.right.height) - 1 
		
    elif value > t.value:
      t.right = self.__remove_rec(value, t.right)
      if t.left == None and t.right == None:
        t.height = 1
      elif t.left == None and t.right is not None:
        t.height = t.right.height - 1
      elif t.right == None and t.left is not None:
        t.height = t.left.height - 1
      else:
        t.height = max(t.left.height, t.right.height) + 1     
	
    return t
	
	
	

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return '[ ]'
    else:
      string = '['
      string = self.__in_order(string, self.__root)
      return string[:-1] + ' ]'
	  
  def __in_order(self, string, node):
    if node is not None:
      string = self.__in_order(string, node.left)
      string = string + ' ' + str(node.value) + ','
      string = self.__in_order(string, node.right)
    return string
	  
	def __balance(self, t):
    if t == None:
      return t
    elif t.left.height - t.right.height == 2:
      if t.right.right.height - t.right.left == 1 or t.right.right.height - t.right.left == 0:
        temp = t.right
        if temp.left != None:
          float = temp.left
          temp.left = t
          t.right = float
          t = temp
          return t 
        else:
          temp.left = t
          t = temp
          return t 
      elif t.right.right.height - t.right.left.height == -1:
        temp = t.right 
        t.right = temp.left
        t.right.right = temp
        
        if temp.left != None:
          float = temp.left
          temp.left = t
          t.right = float 
          t = temp
        else:
          temp.left = t
          t = temp
          return t 
	  elif t.right.height - t.left.height == -2:
      if t.left.right.height - t.left.left.height == -1 or t.left.right.height - t.left.left.height == 0:
        temp = t.left
        if temp.right != None:
          float = temp.right
          temp.right = t
          t.left = float 
          t = temp
          return t 
        else:
          temp.right = t 
          t = temp
          return t 
      elif t.left.right.height - t.left.left.height == 1:
        temp = t.left 
        t.left = temp.right 
        t.left.left = temp
        
        temp = t.left 
        if temp.right != None:
          float = temp.right 
          temp.right = t 
          t.left = float 
          t = temp
          return t 
        else:
          temp.right = t 
          t = temp
          return t 

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return '[ ]'
    else:
      string = '['
      string = self.__pre_order(string, self.__root)
      return string[:-1] + ' ]'
	  
  def __pre_order(self, string, node):
    if node is not None:
      string = string + ' ' + str(node.value) + ','
      string = self.__pre_order(string, node.left)
      string = self.__pre_order(string, node.right)
    return string
	  

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return '[ ]'
    else:
      string = '['
      string = self.__post_order(string, self.__root)
      return string[:-1] + ' ]'
	  
  def __post_order(self, string, node):
    if node is not None:
      string = self.__post_order(string, node.left)
      string = self.__post_order(string, node.right)
      string = string + ' ' + str(node.value) + ','
    return string
	  

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root is None:
      return 0
    else:
      return self.__root.height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  #Main function calls for simple testing
  temp = Binary_Search_Tree()
  temp.insert_element(10)
  temp.insert_element(15)
  temp.remove_element(10)
  print(temp.get_height())
  print(temp)
   
