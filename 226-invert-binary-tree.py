# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # stopping contition
        if not root:
            return None

        # swap subtrees
        root.left , root.right = root.right, root.left

        # call invertTree on swapped subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
