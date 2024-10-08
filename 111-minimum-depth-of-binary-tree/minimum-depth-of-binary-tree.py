# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def dfs(node, depth):
            isLeaf = not node.left and not node.right
            if isLeaf: return depth
            if node.left and node.right: return min(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
            elif node.left: return dfs(node.left, depth + 1)
            elif node.right: return dfs(node.right, depth + 1)
            
            
        
        return dfs(root, 1)