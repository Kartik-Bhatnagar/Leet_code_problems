#URL : https://leetcode.com/problems/n-ary-tree-postorder-traversal/?envType=daily-question&envId=2024-08-26
#[Easy] [590] 
#Title: [ N-ary Tree Postorder Traversal]
#Author: Kartik Bhatnagar
#Date : 2024-08-26 (YYYY-MM-DD)

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        result=[]
        if root is None:
            return result
        
        # print("root",root)
        # print(root.right)
        # print(root.left)
        def dfs(node):
            # print(node.val)
            if len(node.children) ==0 :
                result.append(node.val)
                return
            for c_nod in node.children:
                dfs(c_nod)
            result.append(node.val)
        dfs(root)
        return result
if __name__ == "__main__":
    s=Solution()
