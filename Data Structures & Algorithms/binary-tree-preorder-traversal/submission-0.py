# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []

        def move(node):
            if not node:
                return
            nums.append(node.val)
            move(node.left)
            move(node.right)

        move(root)
        return nums