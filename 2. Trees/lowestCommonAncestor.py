# leetcode 235
# lowest common ancestor of two nodes in a **BINARY** tree
import TreeNode

class Solution:
    def lowestCommonAncestor(self, root:TreeNode, p:TreeNode, q:TreeNode) -> TreeNode:
      if(not root):
          return
      if(root.val == p.val or root.val == q.val):
          return root

      if(root.val < p.val and root.val < q.val):
          return self.lowestCommonAncestor(root.right, p, q)

      if(root.val > p.val and root.val > q.val):
          return self.lowestCommonAncestor(root.left, p, q)

      if((root.val < p.val and root.val > q.val) or 
        (root.val > p.val and root.val < q.val)):
          return root

    def neet_lowestCommonAncestor(self, root:TreeNode, p:TreeNode, q:TreeNode) -> TreeNode:
        cur = root;
        while cur:
            if p.val > root.val and q.val > root.val:
                cur = root.right
            elif p.val < root.val and q.val < root.val:
                cur = root.left
            else:
                return cur