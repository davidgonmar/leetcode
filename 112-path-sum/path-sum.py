# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, acc):
            
            if not node: return False
            acc = acc + node.val
            if (not node.left) and (not node.right): return (acc) == targetSum
            else: return dfs(node.left, acc) or dfs(node.right, acc)
        
        return dfs(root, 0)