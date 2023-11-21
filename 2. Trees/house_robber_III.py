# 337- https://leetcode.com/problems/house-robber-iii/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    # passed most test cases.
    # [2,1,3,null,4]- expected 7 and output 6
    def rob(self, root: Optional[TreeNode]) -> int:
        # foward parse. Robbing level by level
        # Finding the best at each level
        # [a, b, L0, L1, L2]
        a, b = 0, 0
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            total = 0
            for i in range(qlen):
                node = q.popleft()

                if node:
                    q.append(node.left)
                    q.append(node.right)
                    total += node.val
            t = b
            b = max(a + total, b)
            a = t
        return b
