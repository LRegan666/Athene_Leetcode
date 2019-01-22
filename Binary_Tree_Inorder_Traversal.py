class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        self.inorder_travel(root, res)
        return res

    def inorder_travel(self, node, r):
        if not node:
            return
        self.inorder_travel(node.left, r)
        r.append(node.val)
        self.inorder_travel(node.right, r)

