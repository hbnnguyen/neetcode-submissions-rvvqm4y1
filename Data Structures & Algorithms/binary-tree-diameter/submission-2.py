# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getPaths(root):
            if not root:
                return {"leftOrRight" : 0, "leftAndRight": 0, "maxPath": 0}

            if not root.left and not root.right:
                return {"leftOrRight" : 0, "leftAndRight": 0, "maxPath": 0}
            
            left = getPaths(root.left)
            right = getPaths(root.right)

            leftOrRight = 1 + max(left["leftOrRight"], right["leftOrRight"])
            leftAndRight = left["leftOrRight"] + right["leftOrRight"]
            maxPath = max(left["leftAndRight"], right["leftAndRight"])
            
            paths = {"leftOrRight": leftOrRight}

            if root.left and root.right:
                paths["leftAndRight"] = 2 + leftAndRight
            else:
                paths["leftAndRight"] = 1 + leftAndRight
            
            if paths["leftAndRight"] > maxPath:
                paths["maxPath"] = paths["leftAndRight"]
            else:
                paths["maxPath"] = maxPath
    
            return paths
        
        paths = getPaths(root)

        return max(paths["leftAndRight"], paths["leftOrRight"], paths["maxPath"])