# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def trav(node, acc):
            if not node: return acc
            return max(trav(node.left, acc + 1),trav(node.right, acc + 1))

        return trav(root, 0)