class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
      if self.data['dpi']:
         if data['dpi'] < self.data['dpi']:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data['dpi'] > self.data['dpi']:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data