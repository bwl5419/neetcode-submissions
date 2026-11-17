# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {}
        for i,v in enumerate(inorder):
            idx[v] = i
        self.p =0
        def build(l,r):
         if l > r:
            return None
         root = TreeNode(preorder[self.p])
         self.p +=1
         mix = idx[root.val]
         root.left = build(l, mix-1)
         root.right = build(mix+1, r)
         return root
        return build(0, len(inorder) - 1)