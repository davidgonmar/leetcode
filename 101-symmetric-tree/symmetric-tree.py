# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def trav(root, inv, res):
            if not root: return res.append(None)
            res.append(root.val)
            if inv:
                trav(root.left, inv, res)
                trav(root.right, inv, res)
            else:
                trav(root.right, inv, res)
                trav(root.left, inv, res)
        arr1 = []
        trav(root, False, arr1)
        arr2 = []
        trav(root, True, arr2)
        return arr1 == arr2