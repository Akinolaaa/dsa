# Find the kth smallest element in a BST

import TreeNode
import collections;

class Solution:

  def kthSmallestElement(self, root: TreeNode, k: int) -> int :
    # do the interative inorder dfs solution k times

        if not root:
            return root

        n=0
        stack = collections.deque([root])
        node = root
        checked = set()
        while stack:
            while node.left and node.left not in checked:
                node = node.left
                stack.append(node)
            node = stack.pop()
            checked.add(node)
            n += 1
            if n==k:
                return node.val
            
            if node.right and node.right not in checked:
                node = node.right
                stack.append(node)

  def neet_kthSmallestElement(self, root: TreeNode, k: int) -> int :
    
    n=0
    stack = []
    cur = root

    while True:
        while cur:
          stack.append(cur)
          cur = cur.left
        
        cur = stack.pop()
        n += 1
        if n==k:
          return cur.val
        
        cur = cur.right