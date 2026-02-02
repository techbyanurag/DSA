# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root,res):
    if root is None:
        return res
    if root.left:
        inorder(root.left,res)
    res.append(root.val)
    if root.right:
        inorder(root.right,res)
    return res
    
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        res=[]
        res=inorder(root,res)
        minAbs=float("inf")
        n=len(res)
        #After we get the inorder traveral , we need to compare the 
        #Absolute difference between alternate elements. And store the minimum  Absolute value`code`
        for i in range(1,n):
            if (res[i]-res[i-1])<minAbs:
                minAbs=res[i]-res[i-1]
        return minAbs
