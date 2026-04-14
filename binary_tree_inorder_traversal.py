class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        while root:
            if root.left is None:
                ans.append(root.val)
                root=root.right
            else:
                prev=root.left
                while prev.right and prev.right!=root:
                    prev=prev.right
                if prev.right is None:
                    prev.right=root
                    root=root.left
                else:
                    ans.append(root.val)
                    prev.right=None
                    root=root.right
        return ans
