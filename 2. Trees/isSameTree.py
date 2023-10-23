import TreeNode

class Solution:

  def isSameTree(self, r: TreeNode, t: TreeNode):
    if not r and not t:
      return True;

    if not r or not t or r.value != t.value:
      return False
    
    if r.value == t.value:
      return True
  
    return self.isSameTree(r.left, t.left) and self.isSameTree(r.right, t.right)