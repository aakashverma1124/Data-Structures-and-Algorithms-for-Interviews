#
# @author
# aakash.verma
#

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder = []
        stack1 = []
        stack2 = []
        if root is None:
            return postorder
        stack1.append(root)
        while len(stack1) != 0:
            current = stack1.pop()
            stack2.append(current)
            if current.left is not None:
                stack1.append(current.left)
            if current.right is not None:
                stack1.append(current.right)

        while len(stack2) != 0:
            postorder.append(stack2.pop().val)

        return postorder

if __name__ == '__main__':
    .
    .
    .