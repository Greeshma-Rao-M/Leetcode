class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root:
            count=1
            if root.left:
                count+=self.countNodes(root.left)
            if root.right:
                count+=self.countNodes(root.right)
            return count
        else:
            return 0
