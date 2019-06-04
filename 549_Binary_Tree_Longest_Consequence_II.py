"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    http://bookshadow.com/weblog/2017/04/09/leetcode-binary-tree-longest-consecutive-sequence-ii/
    https://www.cnblogs.com/lightwindy/p/9801750.html
    """
    def solve(self,root):
        asc=0#ascending count
        des=0#descending count
        for child in (root.left,root.right):
            if not child:
                continue
            cAsc,cDes = self.solve(child)
            if child.val == root.val -1:
                des = max(des,cDes)
            elif child.val ==root.val +1:
                asc=max(asc,cAsc)
        self.ans = max(self.ans,asc+des+1)
        return asc+1,des+1
    def longestConsecutive2(self, root):
        # write your code here
        self.ans = 0
        if root:
            self.solve(root)
            return self.ans 
