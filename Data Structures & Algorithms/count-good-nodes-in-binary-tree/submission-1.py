# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodnode = 0

        def compare(node,max_val = float('-inf')):
            nonlocal goodnode
            if not node:
                return 0

            if node.val >= max_val:
                goodnode += 1
                max_val = node.val

            compare(node.left, max_val)
            compare(node.right,max_val)

        compare(root, max_val=float('-inf'))
        return goodnode