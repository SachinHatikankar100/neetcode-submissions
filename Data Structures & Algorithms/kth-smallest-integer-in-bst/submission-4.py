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
        # arr = []

        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)
        
        # dfs(root)
        # return arr[k-1]

        #Recursive DFS Optimal Approach
        # cnt = k
        # res = root.val

        # def dfs(node):
        #     nonlocal cnt, res
        #     if not node:
        #         return
        #     dfs(node.left)
        #     if cnt==0:
        #         return 
        #     cnt -= 1
        #     if cnt==0:
        #         res = node.val
        #         return
        #     dfs(node.right)
        
        # dfs(root)
        # return res 

        #Iterative DFS Optimal Approach
        # stack = []
        # curr = root
        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     k -= 1
        #     if k==0:
        #         return curr.val
        #     curr = curr.right

        #Morris Traversal Approach
        curr = root
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -= 1
                    if k==0:
                        return curr.val
                    curr = curr.right
        return -1
