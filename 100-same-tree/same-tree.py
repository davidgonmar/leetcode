# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def trav(node, res):
            if (not node): return res.append(None)
            res.append(node.val)
            trav(node.left, res)
            trav(node.right, res)
        
        arr1 = []
        trav(p, arr1)

        arr2 = []
        trav(q, arr2)

        return arr1 == arr2