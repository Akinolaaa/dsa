# leetcode 102
# return the level order traversal of a tree

import TreeNode
from collections import deque;

class Solution:

  def isSameTree(self, root: TreeNode)-> list[list[int]]:
    if(not root):
        return root
    res = [[root.val]]
    temp = [root]

    while len(temp) > 0:
        children = []
        vals = []
        for n in temp:
            if(n.left):
                children.append(n.left)
                vals.append(n.left.val)
            if(n.right):
                children.append(n.right)
                vals.append(n.right.val)
        if(not vals):
            break
        res.append(vals)
        temp = children
    return res

  def neet_isSameTree(self, root: TreeNode)-> list[list[int]]: 
      res = []
      q = deque();
      q.append(root);

      while q:
        qlen = len(q);
        level = []
        for i in range(qlen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level:
                res.append(level)
                
      return res

    



