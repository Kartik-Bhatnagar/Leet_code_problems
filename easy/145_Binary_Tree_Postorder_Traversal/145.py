#URL : https://leetcode.com/problems/binary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-25
#[Easy] [145] 
#Title: [ Binary Tree Postorder Traversal]
#Author: Kartik Bhatnagar
#Date : 2024-08-25 (YYYY-MM-DD)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root) -> list[int]:
        result=[]
        if root is None:
            return result
        
        # print("root",root)
        # print(root.right)
        # print(root.left)
        def dfs(node):
            # print(node.val)
            if node.left is None and node.right  is None:
                result.append(node.val)
                return
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result
if __name__ == "__main__":
    s=Solution()
