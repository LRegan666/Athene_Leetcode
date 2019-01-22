class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.checkSymmetric(root, root)

    def checkSymmetric(self, node1, node2):
        if not node1 and not node2:
            return True
        if (node1 and node2) and (node1.val == node2.val):
            return self.checkSymmetric(node1.left, node2.right) and self.checkSymmetric(node1.right, node2.left)
        return False


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


if __name__ == '__main__':
    input = "[1,2,3,3,null,2,null]"
    root = stringToTreeNode(input)
    ret = Solution().isSymmetric(root)
    print(ret)

