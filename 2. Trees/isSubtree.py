# // leetcode 572

class Solution:

  def isSameTree(self, r, t):
    if not r and not t:
      return True;

    if not r or not t or r.value != t.value:
      return False
    
    if r.value == t.value:
      return True
  
    return self.isSameTree(r.left, t.left) and self.isSameTree(r.right, t.right)
  
  def isSubtree(self, root, subRoot):
    if(not root and subRoot):
      return False
    
    if(not subRoot):
      return True

    if(self.isSameTree(root, subRoot)):
      return True

    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    
    
