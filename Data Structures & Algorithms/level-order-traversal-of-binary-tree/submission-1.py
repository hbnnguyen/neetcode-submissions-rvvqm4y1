# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
            
        # out = [[root]]
        # res = [[root.val]]
        
        # for lvl in out:
        #     new_lvl = []
        #     vals = []

        #     for node in lvl:
        #         if node.left:
        #             new_lvl.append(node.left)
        #             vals.append(node.left.val)
        #         if node.right:
        #             new_lvl.append(node.right)
        #             vals.append(node.right.val)
            
        #     if len(new_lvl) > 0:
        #         out.append(new_lvl)
        #         res.append(vals)
        
        # return res

        if not root:
            return []
        
        lvl = [root]
        out = []

        while lvl:
            new_lvl = []
            vals = []
            for node in lvl:
                if node.left:
                    new_lvl.append(node.left)
                if node.right:
                    new_lvl.append(node.right)
                vals.append(node.val) 
            
            out.append(vals)
            lvl = new_lvl
        
        return out
            