# leetcode 133- clone-graph
from typing import Optional
class Node:
   def __init__(self, val = 0, neighbors = None):
      self.val = val
      self.neighbors = neighbors if neighbors is not None else []

class Solution:
   def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
      print('Cloning graph...')

      visited = {}
      def dfs(n):
            if(n == None):
               return n
            new_node = Node(n.val)
            visited[n.val] = new_node
            for neigh in n.neighbors:
               if(neigh.val not in visited):
                  child = dfs(neigh)
               else:
                  child = visited[neigh.val]
               new_node.neighbors.append(child)

            return new_node
            
      return dfs(node)

solution = Solution()
random_node = Node(23);
solution.cloneGraph(random_node)
