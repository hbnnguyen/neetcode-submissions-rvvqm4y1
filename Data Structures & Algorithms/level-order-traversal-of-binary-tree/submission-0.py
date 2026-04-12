# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        res = []

        if not root:
            return out
        else:
            out.append([root])
            res.append([root.val])
        
        for lvl in out:
            new_lvl = []
            vals = []

            for node in lvl:
                root = node

                if node.left:
                    new_lvl.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    new_lvl.append(node.right)
                    vals.append(node.right.val)
            
            if len(new_lvl) > 0:
                out.append(new_lvl)
                res.append(vals)
        
        
    
        return res

        


        