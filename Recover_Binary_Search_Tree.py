class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        nodes = []
        self._inorder_collector(root, nodes)
        n1, n2 = None, None
        for i in range(1, len(nodes)):
            if nodes[i-1].val > nodes[i].val:
                if n1 is None:
                    n1 = nodes[i-1]
                else:
                    n2 = nodes[i]
        if n2 is None:
            n2 = nodes[nodes.index(n1)+1]
        tmp = n2.val
        n2.val = n1.val
        n1.val = tmp

    def _inorder_collector(self, root, nodes):
        if not root:
            return
        if root.left:
            self._inorder_collector(root.left, nodes)
        nodes.append(root)
        if root.right:
            self._inorder_collector(root.right, nodes)

    def recoverTree_single(self, root):
        cur_node = None
        n1, n2 = None, None
        _, n1, n2 = self._inorder_swap(root, cur_node, n1, n2)
        tmp = n2.val
        n2.val = n1.val
        n1.val = tmp

    def _inorder_swap(self, root, cur_node, n1, n2):
        if not root:
            return
        if root.left:
            cur_node, n1, n2 = self._inorder_swap(root.left, cur_node, n1, n2)
        if cur_node is not None and cur_node.val > root.val:
            if not n1:
                n1, n2 = cur_node, root
            else:
                n2 = root
        cur_node = root
        if root.right:
            cur_node, n1, n2 = self._inorder_swap(root.right, cur_node, n1, n2)
        return cur_node, n1, n2
