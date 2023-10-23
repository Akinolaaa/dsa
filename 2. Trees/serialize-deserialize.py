class TreeNode:
    
  def __init__(self, val) -> None:
    self.left = None;
    self.right = None;
    self.value = val

import collections;

class Codec:

    def serialize(self, root):
      """Encodes a tree to a single string.
      
      :type root: TreeNode
      :rtype: str
      """
      nodes = [root]
      q = collections.deque([root])

      while(len(q) > 0) :
        n = q.popleft()
        if n:
          q.append(n.left)
          q.append(n.right)
          nodes.append(n.value)
        else:
          nodes.append('none')
  
      return nodes

    def deserialize(self, data):
      """Decodes your encoded data to tree.
      
      :type data: str
      :rtype: TreeNode
      """
      # data is a bfs array
      i = 0
      while(i < len(data)):
        if(data[i] != 'none'){
          root = TreeNode(data[i]);
        }

      return root;

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e

solu = Codec()
print(solu.serialize(a))
