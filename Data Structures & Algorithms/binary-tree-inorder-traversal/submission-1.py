# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        alist = []

        def move(node):
            if not node:
                return 
            move(node.left)
            alist.append(node.val)
            move(node.right)

        move(root)
        return alist