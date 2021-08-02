#
# @author
# aakash.verma
#

class InorderTraversal:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []
        stack = []
        if root is None:
            return inorder
        curr = root
        while curr is not None or len(stack) != 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
        return inorder

if __name__ == '__main__':
    .
    .
    .