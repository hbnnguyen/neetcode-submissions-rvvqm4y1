# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getPaths(root):
            if not root or (not root.left and not root.right):
                return {"leftOrRight" : 0, "maxPath": 0}

            left = getPaths(root.left)
            right = getPaths(root.right)

            leftOrRight = 1 + max(left["leftOrRight"], right["leftOrRight"])
            leftAndRight = left["leftOrRight"] + right["leftOrRight"]
            
            paths = {"leftOrRight": leftOrRight}

            if root.left:
                leftAndRight += 1
            if root.right:
                leftAndRight += 1
            
            paths["maxPath"] = max(leftAndRight, left["maxPath"], right["maxPath"])
    
            return paths
        
        paths = getPaths(root)

        return max(paths["leftOrRight"], paths["maxPath"])