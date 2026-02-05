class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d=0
        def help(node):
            if not node:
                return 0
            lh=help(node.left)
            rh=help(node.right)
            self.d=max(self.d,lh+rh)
            return 1+max(lh,rh)
        help(root)
        return self.d
