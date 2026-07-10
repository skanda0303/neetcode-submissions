# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        def calculatesum(node):
            nonlocal summ
            if node is None:
                return
            if node.val >= low and node.val <= high:
                summ+= node.val
            calculatesum(node.left)
            calculatesum(node.right)



        val = calculatesum(root)
        return summ