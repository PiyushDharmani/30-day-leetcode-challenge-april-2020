# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # make first element root
        root = TreeNode(preorder[0])
        # initialize a stack with root
        stack = [root]

        for current in preorder[1:]:
            # when current is less than top of stack
            if current < stack[-1].val:
                stack[-1].left = TreeNode(current)
                stack.append(stack[-1].left)
            #when value is more than top of stack
            else:
                # pop until current is greater than top of stack
                while stack and current > stack[-1].val:
                    top = stack.pop()
                top.right = TreeNode(current)
                stack.append(top.right)
        
        return root
