# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = -float('inf')

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.result = max(self.result,root.val+left+right)
            return max(0,root.val+max(left,right))
        helper(root)
        return self.result
