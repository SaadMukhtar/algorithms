# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, smaller, bigger):
            if not node:
                return True
            if node.val >= smaller or node.val <= bigger:
                return False
            return check(node.left, node.val, bigger) and check(node.right, smaller, node.val)
        return check(root, float('inf'), float('-inf'))
