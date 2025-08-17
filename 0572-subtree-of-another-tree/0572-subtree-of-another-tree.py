# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not r:return False
        if not s:return True

        if self.sameTree(r,s):
            return True
        return (self.isSubtree(r.left,s) or self.isSubtree(r.right,s))

    def sameTree(self,r,s):
        if not s and not r:
            return True
        if s and r and s.val==r.val:
            return (self.sameTree(s.left,r.left) and self.sameTree(s.right,r.right))
        return False
        