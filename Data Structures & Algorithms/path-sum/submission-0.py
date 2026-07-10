# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        flag = False
        def findpath(node,curr_sum):
            nonlocal flag
            if node is None:
                return
            curr_sum += node.val
            if node.left is None and node.right is None:
                if curr_sum == targetSum:
                    flag = True
            findpath(node.left,curr_sum)
            findpath(node.right,curr_sum)


        findpath(root,0)
        return flag