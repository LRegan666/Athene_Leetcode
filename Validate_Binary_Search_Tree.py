class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        res = []
        return self.inorder_travel(root, res)

    def inorder_travel(self, node, res):
        if not node:
            return True
        left = self.inorder_travel(node.left, res)
        if not res or node.val > res[-1]:
            res.append(node.val)
            mid = True
        else:
            mid = False
        right = self.inorder_travel(node.right, res)
        return left and mid and right
