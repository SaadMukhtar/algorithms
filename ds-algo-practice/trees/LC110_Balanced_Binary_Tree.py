# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def balance(node):
            if not node:
                return True, 0
            lBalance, left = balance(node.left)
            rBalance, right = balance(node.right)
            if not lBalance or not rBalance or abs(left - right) > 1:
                return False, 0
            return True, 1+max(left, right)

        balanced, height = balance(root)
        return balanced