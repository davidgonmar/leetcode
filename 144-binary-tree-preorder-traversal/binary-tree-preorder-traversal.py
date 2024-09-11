# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.iterative(root)
    
    def iterative(self, root):
        if root is None:
            return
        stack = [root]
        acc = []
        while (stack):
            curr = stack.pop()
            acc.append(curr.val)
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)

        
        return acc


    def recursive(self, root):
        acc = []
        def preorderTraversal(node, acc):
            if (node):
                acc.append(node.val)
                preorderTraversal(node.left, acc)
                preorderTraversal(node.right, acc)

        preorderTraversal(root, acc)
        return acc
    