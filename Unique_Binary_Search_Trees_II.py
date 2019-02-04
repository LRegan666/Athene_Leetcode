class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        trees = self.collect_bst(1, n)
        return trees

    def collect_bst(self, s, e):
        res = []
        if s > e:
            res.append(None)
            return res
        for i in range(s, e+1):
            left_nodes = self.collect_bst(s, i-1)
            right_nodes = self.collect_bst(i+1, e)
            for left in left_nodes:
                for right in right_nodes:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res
