# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkBST(node, minimum=float("-inf"), maximum=float("inf")):
            if not node:
                return True
            if not (minimum < node.val < maximum):
                return False
            return checkBST(node.left, minimum, node.val) \
                and checkBST(node.right, node.val, maximum)
        return checkBST(root)
            