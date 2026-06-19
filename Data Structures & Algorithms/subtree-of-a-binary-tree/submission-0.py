# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(r, sr):
            if not r or not sr:
                return False
            if r and sr and r.val == sr.val:
                return isequal(r,sr)
            return dfs(r.left, sr) or dfs(r.right, sr)
                
            
        def isequal(n1,n2):
            if not n1 and not n2:
                return True
            if n1 and n2 and n1.val == n2.val:
                return isequal(n1.left,n2.left) and isequal(n1.right,n2.right)
            else:
                return False

        return dfs(root,subRoot)