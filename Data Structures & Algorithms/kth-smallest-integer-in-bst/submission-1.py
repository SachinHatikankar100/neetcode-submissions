# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Brute Force Approach
        # arr = []

        # def dfs(node):
        #     if not node:
        #         return
        
        #     arr.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        
        # dfs(root)
        # arr.sort()
        # return arr[k-1]

        #Inorder Traversal Approach
        arr = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return arr[k-1]


        