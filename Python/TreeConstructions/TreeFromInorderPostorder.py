#
# @author 
# aakash.verma
#


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # LeetCode Code
    # Line 18 - 31

    inorder_map = {}
    def solve(postorder, left, right):
            if left > right:
                return None
            rootValue = postorder.pop()
            index = Solution.inorder_map[rootValue]
            root = TreeNode(rootValue)
            root.right = Solution.solve(postorder, index + 1, right)
            root.left = Solution.solve(postorder, left, index - 1)
            return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        Solution.inorder_map = {val:index for index, val in enumerate(inorder)} 
        return Solution.solve(postorder, 0, len(inorder) - 1)

if __name__ == '__main__':

    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    root = buildTree(inorder, postorder)    
    # We can write the code for BFS traversal to check the formed tree. 