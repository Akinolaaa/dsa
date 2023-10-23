import TreeNode;

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root; #redundant cos you'll always return root regardless
    
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root